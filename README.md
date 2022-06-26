# HYBO: Helping You Be Okay

<hr/>

![](https://cdn.discordapp.com/attachments/939536871262912546/939616419140755496/unknown.png)

<hr/>

## The Problem

<img src="https://cdn.discordapp.com/attachments/939536871262912546/939941143242756096/Screen_Shot_2022-02-06_at_12.49.23_PM.png" width=200>

<br/>

If you’re feeling under the weather, you’re likely to stay home. However, would you do the same when you feel stressed or anxious? Unlike physical health, mental health is often downplayed. By age 40, about 50% of the population will have or have had a mental illness in Canada. According to a study by WHO around 30 to 80% of individuals with mental health issues are hesitant to reach out for treatment due to the stigma surrounding mental disorders.

<hr/>

## The Solution

<img src="https://cdn.discordapp.com/attachments/939536871262912546/939941143846748281/Screen_Shot_2022-02-06_at_12.50.15_PM.png" width=200>

<br/>

HYBO or Helping You Be Okay, simplifies the steps you need to take to improve your mental health. Oftentimes, individuals struggle with seeking help as they are unsure where to start or even if they need treatment. This is where HYBO will help. HYBO provides a quick survey for users to identify their likelihood of having a mental illness. But unlike other apps and tools to help individuals with mental health issues, HYBO prioritizes the users’ boundaries. To help the user feel comfortable and be more honest with the information they share, our survey does not directly ask the user about their feelings, emotions, or behaviours- rather, general, surface-level questions about their lifestyle. 

![](https://cdn.discordapp.com/attachments/889980120461361225/990624114186276935/unknown.png)

HYBO breaks down the negative connotations linked with mental health treatment by providing the user with a comfortable experience that allows them to only share aspects of their life; such as income level, sociodemographics, and so forth. Instead of overwhelming the user with deep questions about their emotions, HYBO depicts mental health in a less vulnerable & more neutral fashion. Thanks to our innovative AI technology, HYBO provides an accurate reading of the user’s emotions as the data improves each time the survey is filled out. Based on their responses, HYBO supports the user’s needs with forms of subtle mental health treatment depending on their current state of mind/emotions, such as meditation, relaxing music and even games.  

![](https://cdn.discordapp.com/attachments/889980120461361225/990624492705415208/unknown.png)

<hr/>

## Impact

This project provides a unique service to those in need of assistance when it comes to mental health. We believe that HYBO can remove some of the stigma surrounding mental health and lead people to receive professional help. It introduces people to the world of therapy in an accessible way and demonstrates the difference that therapy can bring to your quality of life. HYBO is a fully functional prototype and can be developed further to suit the needs of more people. 

![](https://cdn.discordapp.com/attachments/939536871262912546/939945537581490196/unknown.png)

<hr/>

## Technology Used

We used a number of technologies behind the scenes to make this project easy to use and powerful. In the website we chose to use tailwind css and react. Tailwind allowed me to apply beautiful styling to the website and react gave the powerful features I needed to make it scalable and robust. 
The user interface for the submission form is powered by streamlit. Streamlit gave the flexibility to connect the frontend to the machine learning models in the back.

![](https://cdn.discordapp.com/attachments/939536871262912546/939945490592710717/unknown.png)

Now let's talk about the heart of the project, the machine learning model. We needed data to train a machine learning model, so we used the results of a survey taken by the National Alliance on Mental Illnesses.

![](https://cdn.discordapp.com/attachments/890026036790702101/990640911367155792/unknown.png)

The data had quirks like missing values, skewed columns and large ranges. We fixed this by removing null columns, encoding the categorical variables and Normalizing the data. I also dived deep into analyzing the data and created several reports to summarize the results. You can find all the analysis under the Reports section of the repository. Please feel free to check out the reports and learn more about the data. You can also take a look at the Loading and Preprocessing notebooks if you want to see the code.

![](https://cdn.discordapp.com/attachments/890026036790702101/990639843816140860/unknown.png)

For the predictor, I tried several different models. Ensembles of tree-based models like XGBosst, CatBoost and RandomForests gave the best accuracy. You can find detailed comaprisons between all the models under the ./Reports/MLJAR section of the repository. It contains all the information I used to select the best model. I stayed away from neural networks because the dataset we had was relatively small and the risk of overfitting was high. We trained 3 different models to predict Anxiety, Depression and Compulsive behavior based on the user's response. Check out the Preprocessing and Modeling notebooks and MLJAR reports to see how the models were trained. 

![](https://cdn.discordapp.com/attachments/890026036790702101/990639109129265203/unknown.png)

The final accuracies we got were satisfactory with every model scoring above 85%. The predictions from these models are used to provide tangible steps to the user to make them feel better. 

![](https://cdn.discordapp.com/attachments/890026036790702101/990639543160033301/unknown.png)

<hr/>

## Future Improvements

I beleive that HYBO has immense potential and a few steps in the right direction can take it to the next level. The following steps are the improvements I hope to make to HYBO in thecoming weeks:

1. Improve accuracy of the ML models by collecting more data and testing additional model architectures.

2. Identify addittional mental illnesses to make the results more tailored to the user.

3. Make suggestions more robust to better console the user.

4. Add recommendations for available therapy near the user or online.

5. Make the UI more streamlined (move from streamlit to react).