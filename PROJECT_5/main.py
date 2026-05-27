# SCREENSHORT USING PYTHON
import pyscreenshot

# Capture the full screen
image = pyscreenshot.grab()

# display the image
image.show()
# Save the screenshot to a file
image.save("screenshot.png")
