import sys
print("Python started", flush=True)
try:
    import cv2
    print(f"OpenCV imported: {cv2.__version__}", flush=True)
except Exception as e:
    print(f"OpenCV import failed: {e}", flush=True)
