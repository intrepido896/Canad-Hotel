






translator.py a directory
server my package with
__init___.py



from flask import Flask, request, render_template

# Declare a Flask app
app = Flask(__name__) 
# Main function 
# ------------------
	

#type of function


@app.route('/', methods=['GET', 'POST'])

# provide root endpoint which renders index.html

@app.route('/index.html')


# provide root endpoint  translate from english to frech

app.route('/trans1')

# provide root endpoint translate from french to english


app.route('/trans2')

def main(): 

# If a form is submitted
 if request.method == "POST": 
 
 
  # Get values through input bars 
  Function = request.form.get("Function")
  
  
  
  
    
    

    
    if Function==0 :(
	print ("English to French")
	
	def trans1(Function,text)
	
	import json 
	from ibm_watson import LanguageTranslatorV3 
	from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
 authenticator = IAMAuthenticator('{apikey}') 
 language_translator = LanguageTranslatorV3
 ( version='2018-05-01', authenticator=authenticator )
  language_translator.set_service_url('{url}') 
  translation = language_translator.translate( 
  	 text=request.form.get("text"), 
  	model_id='en-fr').get_result() 
  	translate=(json.dumps(translation, indent=2, ensure_ascii=False))
	 
	  # Get translate
	  
	    return render_template("index.html", output = translate)
	)

elif Function==1: (
	print ("French to English")
	
		def trans2(Function,text)
		import json 
	from ibm_watson import LanguageTranslatorV3 
	from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
 authenticator = IAMAuthenticator('{apikey}') 
 language_translator = LanguageTranslatorV3
 ( version='2018-05-01', authenticator=authenticator )
  language_translator.set_service_url('{url}') 
  translation = language_translator.translate( 
  	 text=request.form.get("text"), 
  	model_id='fr-en').get_result() 
  	translate=(json.dumps(translation, indent=2, ensure_ascii=False))
	 
	  # Get translate
	  
	    return render_template("index.html", output = translate)
	
	
	
	
)

else:(
	
	 print ("Enter valid Function")
)

    
    
    
    
    
  



 # Running the app
	 if __name__ == '__main__
app.run(debug=true)




