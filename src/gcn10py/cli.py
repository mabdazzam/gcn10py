import subprocess
import sys
import os
import platform
from pathlib import Path

def get_executable_path():
    """Return the path to the gcn10 executable, bundled with the package."""
    package_dir = Path(__file__).parent

    # use platform-appropriate executable
    exe_name = "gcn10.exe" if platform.system() == "Windows" else "gcn10"
    exe_path = package_dir / exe_name
    if not exe_path.is_file():
        raise FileNotFoundError(f"gcn10 executable not found at {exe_path}")

    # ensure executable permissions on Unix systems
    if platform.system() != "Windows":
        os.chmod(exe_path, 0o755)
    return str(exe_path)

def run(args=None):
    """
    Run the gcn10 executable with the provided arguments.
    
    Args:
        args (list): List of command-line arguments
        (e.g., ['-c', 'config.txt', '-l', 'block_ids.txt', '-o', 'overwrite']).
                     If None, uses sys.argv[1:].
    
    Returns:
        subprocess.CompletedProcess: Result of the gcn10 execution.
    
    Raises:
        subprocess.CalledProcessError: If gcn10 returns a non-zero exit code.
        FileNotFoundError: If the gcn10 executable is not found.
    """
    if args is None:
        args = sys.argv[1:]
    
    try:
        exe_path = get_executable_path()

        # construct command with executable path and args
        cmd = [exe_path] + args

        # run gcn10, cpature std. out and err 
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )

        # print stdout
        if result.stdout:
            print(result.stdout, end="")
        if result.stderr:
            print(result.stderr, end="", file=sys.stderr)
        return result
    except subprocess.CalledProcessError as e:

        # print err and re-raise
        print(f"Error running gcn10: {e.stderr}", file=sys.stderr)
        raise
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        raise

if __name__ == "__main__":
    run()
