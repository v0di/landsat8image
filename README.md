# Wha does it do?
Given a location and a date, it uses the Nasa Earth API to show a photo taken by the Landsat 8 satellite. The script must be executed on the command-line.

# Set up
Before using the script, you must have access to the Nasa's API key. You can quickly get a key in https://api.nasa.gov/.
After that, save your key as an environment variable. Then, you are good to go.

# How to use
<p>In the same directory where the script is saved, run the following code on the command-line:</p> 
<h3>get_image.py -LAT [latitude] -LON [longitude] -DATE [date] --info</h3>
<p>-DATE and --info are optional. -DATE defaults to today.</p>
<p>If --info is provided, then the latitude and longitude you input are written onto the image.</p>

# Example
<h2>By running the following line</h2>
<img src="examples/example1.jpg">
<div></div>
<h2>you get this image</h2>
<img src="examples/img1.jpg">
