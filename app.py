# import streamlit as st
import json
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
app = Flask(__name__)
CORS(app)

# st.title('Edumate')


df = pd.read_csv('Final.csv')

# course_list=df.subject.unique().tolist()
# course_list.sort()
# course_list.insert(0,'Select a Skill')


# option = st.selectbox('Select a skill', course_list)
# st.write('You selected:', option)
def model(option):
    if option=='Select a Skill':
        df1=df.drop(['course_id','num_subscribers','published_timestamp','subject'],axis=1 )
    else:
        df2=df[df['subject']=='Web Development'].sort_values('num_reviews', ascending=[0])
        df1=df2.head().drop(['course_id','num_subscribers','published_timestamp','subject'], axis=1)
    jsonfiles = json.loads(df1.to_json(orient='records'))
    return jsonfiles
    

@app.route('/', methods=['GET'])
def recommend_movies():
    res = model(request.args.get('q'))
    return jsonify(res)


if __name__ == '__main__':
    app.run(port=5000, debug=True)