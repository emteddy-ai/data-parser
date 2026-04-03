import json
import logging
import os
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


def read_json_file(file_path: str) -> Optional[Dict[str, Any]]:
    """
    Reads a JSON file and returns its content as a dictionary.

    Args:
        file_path: The path to the JSON file.

    Returns:
        A dictionary representing the JSON content, or None if an error occurs.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON format in file: {file_path}")
        return None
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {e}")
        return None


def write_json_file(file_path: str, data: Dict[str, Any]) -> bool:
    """
    Writes a dictionary to a JSON file.

    Args:
        file_path: The path to the JSON file.
        data: The dictionary to write.

    Returns:
        True if the write was successful, False otherwise.
    """
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        logger.error(f"Error writing to file {file_path}: {e}")
        return False


def create_directory_if_not_exists(directory_path: str) -> bool:
    """
    Creates a directory if it does not already exist.

    Args:
        directory_path: The path to the directory.

    Returns:
        True if the directory was created or already exists, False otherwise.
    """
    try:
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        return True
    except Exception as e:
        logger.error(f"Error creating directory {directory_path}: {e}")
        return False


def sanitize_filename(filename: str) -> str:
    """
    Sanitizes a filename by removing or replacing invalid characters.

    Args:
        filename: The filename to sanitize.

    Returns:
        The sanitized filename.
    """
    # Replace spaces with underscores
    filename = filename.replace(" ", "_")
    # Remove characters that are not alphanumeric, underscore, or dot
    filename = ''.join(c for c in filename if c.isalnum() or c == '_' or c == '.')
    return filename