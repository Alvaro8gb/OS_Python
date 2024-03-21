import os

symlink_path = 'data/hola'

try:
  target_path = os.readlink(symlink_path)
  print(f"The symbolic link '{symlink_path}' points to: {target_path}")
except OSError as e:
  print(f"Error: {e}")