import mufem

from mufem import Bnd, Vol
from mufem.electromagnetics.timedomainmagnetic import (
    TangentialMagneticFieldBoundaryCondition,
    TimeDomainMagneticGeneralMaterial,
    TimeDomainMagneticModel,
)

from typing import List

sim = mufem.Simulation.New("Compumag Team1b: Felix Cylinder", "geometry.mesh")

# Setup Problem
mufem.UnsteadyRunner(total_time=0.02, time_step_size=0.001, total_inner_iterations=2)

magnetic_model = TimeDomainMagneticModel(
    marker=["Air", "Cylinder"] @ Vol, order=1, magnetostatic_initialization=True
)

# Setup Materials
air_material = TimeDomainMagneticGeneralMaterial.SimpleVacuum(
    "Air Material", "Air" @ Vol
)

copper_material = TimeDomainMagneticGeneralMaterial.SimpleNonMagnetic(
    "Al", "Cylinder" @ Vol, 25380710.659898475
)
magnetic_model.addMaterials([air_material, copper_material])

# Setup Boundary Conditions
cff_fall = mufem.CffExpressionScalar("79577.488101574*exp(-time()/0.0069)")
cff_zero = mufem.CffConstantScalar(0.0)

cff_magnetic_field = mufem.CffVectorComponent(cff_zero, cff_fall, cff_zero)

tangential_magnetic_field_bc = TangentialMagneticFieldBoundaryCondition(
    "ExternalField", "Air::Boundary" @ Bnd, cff_magnetic_field
)
magnetic_model.addCondition(tangential_magnetic_field_bc)

# Setup Reports
ohmic_heating_report = mufem.VolumeIntegralReport(
    "Ohmic Heating", "Cylinder" @ Vol, "OhmicHeating"
)
sim.getReportManager().addReport(ohmic_heating_report)


ohmic_heating_monitor = mufem.ReportMonitor("Ohmic Heating Monitor", "Ohmic Heating")
sim.getMonitorManager().addMonitor(ohmic_heating_monitor)


sim.run()

# Plot the losses

import pylab

monitor_values = ohmic_heating_monitor.getValues()


values = [(value[0], value[1].getScalarValue()) for value in monitor_values]


pylab.clf()

power_loss_reference = pylab.loadtxt("data/PowerLoss.csv", delimiter=",")

pylab.plot(
    power_loss_reference[:, 0],
    power_loss_reference[:, 1],
    "k-",
    label="Davey et al.",
    linewidth=2.5,
    markersize=6.5,
)

pylab.plot(
    *zip(*values),
    "r.-",
    label="$\\mu$fem",
    markersize=6.5,
    linewidth=2.0,
)

pylab.xlabel("Time t [s]")
pylab.ylabel("Ohmic Heating Loss P$_\\Omega$ [W]")
pylab.xlim(0, 0.02)
pylab.xticks([0, 0.01, 0.02])
pylab.ylim(0, 600)
pylab.legend(loc="best").draw_frame(False)

pylab.savefig(f"OhmicHeating.png")
