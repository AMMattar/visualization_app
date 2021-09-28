# the main problem is receiving data from user and then use it as a visualization items,
# and then need to delete them, will delete instead of saving data over time.
# data will be csv and images
# need to check streamlit documentation if i can do this other wise it will be a flask app.
from flask import Flask, render_template, request, redirect
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import base64
from io import BytesIO

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        d = int(request.form['number'])
        N = int(request.form['N_number'])
        ads_selected = []
        if request.files:
            csv = request.files['CSVfile']
            dataset = pd.read_csv(csv)
            image1 = request.files['pic1']
            image2 = request.files['pic2']
            image3 = request.files['pic3']
            image4 = request.files['pic4']
            image5 = request.files['pic5']
            image6 = request.files['pic6']
            image7 = request.files['pic7']
            image8 = request.files['pic8']
            images = [image1, image2, image3, image4,
                      image5, image6, image7, image8]
            work_images = []
            for i in images:
                if i != "":
                    work_images.append(i)
        ##############
        numbers_of_rewards_1 = [0] * d
        numbers_of_rewards_0 = [0] * d
        total_reward = 0
        for n in range(0, N):
            ad = 0
            # Keep track of the maximum reward pulled from the distributions
            max_random = 0
            for i in range(0, d):
                random_beta = random.betavariate(
                    numbers_of_rewards_1[i]+1, numbers_of_rewards_0[i]+1)
                if(random_beta > max_random):
                    max_random = random_beta
                    ad = i
            ads_selected.append(ad)
            reward = dataset.values[n, ad]
            if(reward == 1):
                numbers_of_rewards_1[ad] = numbers_of_rewards_1[ad]+1
            else:
                numbers_of_rewards_0[ad] = numbers_of_rewards_0[ad]+1
            total_reward = total_reward + 1
            ############## visualization #####################
            new_plt = plt.figure()
            plt.hist(ads_selected)
            plt.title('Histogram of ads selections')
            plt.xlabel('Ads')
            plt.ylabel('Number of times each ad was selected')
            plt.show()
            new_plt = plt.figure()
            ######################################################
            assign = []
            for i in range(d):
                x = numbers_of_rewards_0[i] + numbers_of_rewards_1[i]
                assign.append(x)
            ##############
        return render_template('vis.html')
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
