import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

students_df = pd.read_csv('students.csv')
opening_df = pd.read_csv('intern.csv')

students_df['ipk'] = students_df['ipk'].str.replace(',', '.').astype(float)
opening_df['min_gpa'] = opening_df['min_gpa'].str.replace(',', '.').astype(float)

opening_df['period'] = opening_df['period'].apply(lambda x: int(x.split()[0]) * 12 if "year" in x else int(x.split()[0]))

tfidf = TfidfVectorizer()
opening_df['related_course'] = opening_df['related_course'].fillna('')
opening_df['skills'] = opening_df['skills'].fillna('')

job_profiles = tfidf.fit_transform(opening_df['related_course'] + " " + opening_df['skills'])

students_df['major'] = students_df['major'].fillna('')
students_df['fav_course'] = students_df['fav_course'].fillna('')
students_df['skill'] = students_df['skill'].fillna('')

student_profiles = tfidf.transform(students_df['major'] + " " + students_df['fav_course'] + " " + students_df['skill'])

cosine_sim = cosine_similarity(student_profiles, job_profiles)

for idx, row in students_df.iterrows():
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    sim_scores = [i for i in sim_scores if opening_df['min_gpa'].iloc[i[0]] <= row['ipk'] 
                  and opening_df['period'].iloc[i[0]] <= row['years_experience']*12
                  and opening_df['location'].iloc[i[0]] == row['student_location']]
    

    sim_scores = sim_scores[0:3]

    job_indices = [i[0] for i in sim_scores]

    recommended_jobs = opening_df.iloc[job_indices]

    # print(f"Recommendedations for student {idx} are:")
    # print(recommended_jobs)

print(f"Recommendedations for student {20} are:")
print(recommended_jobs)