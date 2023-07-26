from flask import Flask,request,jsonify,render_template
app=Flask(__name__)
from rsp_game import rsp_play
@app.route('/')
def home():
  return render_template('rsp_index.html')
@app.route('/predict',methods=['POST']) 
def predict():
  val=request.form['val'] 
  result=rsp_play(val)
  #print(result)
  return render_template('rsp_index.html',user_text=str(result[0]),computer_text=str(result[1]),result_text=str(result[2]))
if __name__=="__main__":
  app.run(debug=True)