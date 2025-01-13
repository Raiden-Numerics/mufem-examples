import os
import subprocess

def run_cases(base_directory):
    # Walk through the directory structure
    for root, dirs, files in os.walk(base_directory):
        if "case.py" in files:

            # Save the current working directory
            # Note that we run the test in the local directory, so we
            # can easily load the mesh. After the run the directory is
            # restored so we can continue the os.walk.
            original_dir = os.getcwd()

            case_path = os.path.join(root, "case.py")
            print(f"Running case: {case_path}")
            
            # Execute the command
            try:
                os.chdir(root)
                command = "pymufem case.py"
                result = subprocess.run(command, shell=True, check=True, text=True)
                print(f"Success: {case_path}")
            except subprocess.CalledProcessError as e:
                print(f"Error running {case_path}: {e}")
            finally:
                # Return to the original working directory
                os.chdir(original_dir)

if __name__ == "__main__":
    # Define the base directory and command template
    base_directory = "."
    # Run the cases
    run_cases(base_directory)
