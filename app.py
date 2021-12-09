from flask import Flask, render_template, request, jsonify
import requests
import json
import google_streetview.api



app = Flask(__name__)

lat = [41.923489]
lon = [-87.698433]



@app.route("/")

def index():
    lat1 = lat[0]
    lon1 = lon[0]

    params = [{
	 'size': '600x300', # max 640x640 pixels
	 'location': f'{lat1},{lon1}',
	 'heading': '151.78',
	 'pitch': '-0.76',
	 'key' : "AIzaSyD_SpYR5CmwiUCdaIThCLPvpW3MBs0jHMk"
     }]

# Create a results object
    results = google_streetview.api.results(params)
#print(type(results))
    print(results.links)
    imgurl = results.links[0]

# run a request using our params dictionary
    
    return render_template("index.html",imgurl=imgurl)

@app.route('/left', methods=['GET', 'POST'])
def leftCall():
     newLat = lat[-1] - .0001

     newLon= lon[-1]

  #Append the most recent Latitude to the Latitude list so that you can get it on the next call
     lat.append(newLat)

  #Do the api call with the newLat and return a new image url
     url = f'{newLat}/{newLon}'

    #run metadata
     params = [{
	'size': '600x300', # max 640x640 pixels
	'location': f'{newLat},{newLon}',
	'heading': '151.78',
	'pitch': '-0.76',
	'key' : "AIzaSyD_SpYR5CmwiUCdaIThCLPvpW3MBs0jHMk"
    }]
     metaresults = google_streetview.api.results(params,site_metadata= 'https://maps.googleapis.com/maps/api/streetview/metadata')
     print(metaresults.metadata)
    # Define parameters for street view api
     status = metaresults.metadata[0]['status']


     while (status == 'ZERO_RESULTS'):
        lat1 = newLat+.0001

        params = [{
	    'size': '600x300', # max 640x640 pixels
	    'location': f'{lat1},{newLon}',
	    'heading': '151.78',
	    'pitch': '-0.76',
	    'key' : "AIzaSyD_SpYR5CmwiUCdaIThCLPvpW3MBs0jHMk"
        }]

        metaresults2 = google_streetview.api.results(params,site_metadata= 'https://maps.googleapis.com/maps/api/streetview/metadata')
        print(metaresults.metadata)

        status = metaresults2.metadata[0]['status']
        print(status)

        if (status == 'OK'):
            lat.append(lat1)
            break

     newLat = lat[-1]

     newLon= lon[-1]
     
     params = [{
	 'size': '600x300', # max 640x640 pixels
	 'location': f'{newLat},{newLon}',
	 'heading': '151.78',
	 'pitch': '-0.76',
	 'key' : "AIzaSyD_SpYR5CmwiUCdaIThCLPvpW3MBs0jHMk",
    }]
    # Create a results object

     results = google_streetview.api.results(params)
    #print(type(results))
     print(results.links)
     imgurl = results.links[0]

    #return your json file
     Data = {
        'url': imgurl

    }

     return jsonify(**Data) 

@app.route('/up', methods=['GET', 'POST'])
def upCall():
  
     newLat = lat[-1] 

     newLon= lon[-1]+ .0001

  #Append the most recent Latitude to the Latitude list so that you can get it on the next call
     lon.append(newLon)

  #Do the api call with the newLat and return a new image url
     url = f'{newLat}/{newLon}'

    #run metadata
     params = [{
	'size': '600x300', # max 640x640 pixels
	'location': f'{newLat},{newLon}',
	'heading': '151.78',
	'pitch': '-0.76',
	'key' : "AIzaSyD_SpYR5CmwiUCdaIThCLPvpW3MBs0jHMk"
    }]
     metaresults = google_streetview.api.results(params,site_metadata= 'https://maps.googleapis.com/maps/api/streetview/metadata')
     print(metaresults.metadata)
    # Define parameters for street view api
     status = metaresults.metadata[0]['status']


     while (status == 'ZERO_RESULTS'):
        lon1 = newLon+.0001

        params = [{
	    'size': '600x300', # max 640x640 pixels
	    'location': f'{newLat},{lon1}',
	    'heading': '151.78',
	    'pitch': '-0.76',
	    'key' : "AIzaSyD_SpYR5CmwiUCdaIThCLPvpW3MBs0jHMk"
        }]

        metaresults2 = google_streetview.api.results(params,site_metadata= 'https://maps.googleapis.com/maps/api/streetview/metadata')
        print(metaresults.metadata)

        status = metaresults2.metadata[0]['status']
        print(status)

        if (status == 'OK'):
            lon.append(lon1)
            break

     newLat = lat[-1]

     newLon= lon[-1]
     
     params = [{
	 'size': '600x300', # max 640x640 pixels
	 'location': f'{newLat},{newLon}',
	 'heading': '151.78',
	 'pitch': '-0.76',
	 'key' : "AIzaSyD_SpYR5CmwiUCdaIThCLPvpW3MBs0jHMk",
    }]
    # Create a results object

     results = google_streetview.api.results(params)
    #print(type(results))
     print(results.links)
     imgurl = results.links[0]

    #return your json file
     Data = {
        'url': imgurl

    }

     return jsonify(**Data)

@app.route('/right', methods=['GET', 'POST'])
def rightCall():
  
     newLat = lat[-1] + .0001

     newLon= lon[-1]

  #Append the most recent Latitude to the Latitude list so that you can get it on the next call
     lat.append(newLat)

  #Do the api call with the newLat and return a new image url
     url = f'{newLat}/{newLon}'

    #run metadata
     params = [{
	'size': '600x300', # max 640x640 pixels
	'location': f'{newLat},{newLon}',
	'heading': '151.78',
	'pitch': '-0.76',
	'key' : "AIzaSyD_SpYR5CmwiUCdaIThCLPvpW3MBs0jHMk"
    }]
     metaresults = google_streetview.api.results(params,site_metadata= 'https://maps.googleapis.com/maps/api/streetview/metadata')
     print(metaresults.metadata)
    # Define parameters for street view api
     status = metaresults.metadata[0]['status']


     while (status == 'ZERO_RESULTS'):
        lat1 = newLat+.0001

        params = [{
	    'size': '600x300', # max 640x640 pixels
	    'location': f'{lat1},{newLon}',
	    'heading': '151.78',
	    'pitch': '-0.76',
	    'key' : "AIzaSyD_SpYR5CmwiUCdaIThCLPvpW3MBs0jHMk"
        }]

        metaresults2 = google_streetview.api.results(params,site_metadata= 'https://maps.googleapis.com/maps/api/streetview/metadata')
        print(metaresults.metadata)

        status = metaresults2.metadata[0]['status']
        print(status)

        if (status == 'OK'):
            lat.append(lat1)
            break

     newLat = lat[-1]

     newLon= lon[-1]
     
     params = [{
	 'size': '600x300', # max 640x640 pixels
	 'location': f'{newLat},{newLon}',
	 'heading': '151.78',
	 'pitch': '-0.76',
	 'key' : "AIzaSyD_SpYR5CmwiUCdaIThCLPvpW3MBs0jHMk",
    }]
    # Create a results object

     results = google_streetview.api.results(params)
    #print(type(results))
     print(results.links)
     imgurl = results.links[0]

    #return your json file
     Data = {
        'url': imgurl

    }

     return jsonify(**Data)


@app.route('/down', methods=['GET', 'POST'])
def downCall():
  
     newLat = lat[-1]

     newLon= lon[-1] - .0001

  #Append the most recent Latitude to the Latitude list so that you can get it on the next call
     lon.append(newLon)

  #Do the api call with the newLat and return a new image url
     url = f'{newLat}/{newLon}'

    #run metadata
     params = [{
	'size': '600x300', # max 640x640 pixels
	'location': f'{newLat},{newLon}',
	'heading': '151.78',
	'pitch': '-0.76',
	'key' : "AIzaSyD_SpYR5CmwiUCdaIThCLPvpW3MBs0jHMk"
    }]
     metaresults = google_streetview.api.results(params,site_metadata= 'https://maps.googleapis.com/maps/api/streetview/metadata')
     print(metaresults.metadata)
    # Define parameters for street view api
     status = metaresults.metadata[0]['status']


     while (status == 'ZERO_RESULTS'):
        lon1 = newLon+.0001

        params = [{
	    'size': '600x300', # max 640x640 pixels
	    'location': f'{newLat},{lon1}',
	    'heading': '151.78',
	    'pitch': '-0.76',
	    'key' : "AIzaSyD_SpYR5CmwiUCdaIThCLPvpW3MBs0jHMk"
        }]

        metaresults2 = google_streetview.api.results(params,site_metadata= 'https://maps.googleapis.com/maps/api/streetview/metadata')
        print(metaresults.metadata)

        status = metaresults2.metadata[0]['status']
        print(status)

        if (status == 'OK'):
            lon.append(lon1)
            break

     newLat = lat[-1]

     newLon= lon[-1]
     
     params = [{
	 'size': '600x300', # max 640x640 pixels
	 'location': f'{newLat},{newLon}',
	 'heading': '151.78',
	 'pitch': '-0.76',
	 'key' : "AIzaSyD_SpYR5CmwiUCdaIThCLPvpW3MBs0jHMk",
    }]
    # Create a results object

     results = google_streetview.api.results(params)
    #print(type(results))
     print(results.links)
     imgurl = results.links[0]

    #return your json file
     Data = {
        'url': imgurl

    }

     return jsonify(**Data)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
