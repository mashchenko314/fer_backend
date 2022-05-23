import urllib.request
from fer import Video, FER
import pandas as pd
import os
import shutil

def emotion_recognition(url):
    urllib.request.urlretrieve(url, 'record.mp4')
    video_path = '../ademotions/record.mp4'
    face_detector = FER(mtcnn=True)
    input_video = Video(video_path)
    processing_data = input_video.analyze(face_detector, display=True)
    vid_df = input_video.to_pandas(processing_data)
    vid_df = input_video.get_first_face(vid_df)
    vid_df = input_video.get_emotions(vid_df)

    angry = sum(vid_df.angry)
    disgust = sum(vid_df.disgust)
    fear = sum(vid_df.fear)
    happy = sum(vid_df.happy)
    sad = sum(vid_df.sad)
    surprise = sum(vid_df.surprise)
    neutral = sum(vid_df.neutral)

    top_emotion = top(angry, disgust, fear, happy, sad, surprise, neutral)
    emotion_shade = shade(angry, disgust, fear, happy, sad, surprise, neutral)
    percent_emotions = to_percentage(angry, disgust, fear, happy, sad, surprise)
    engagement = is_engagement(percent_emotions)
    analyze_result = {
        'Злость': angry,
        'Отвращение': disgust,
        'Страх': fear,
        'Счастье': happy,
        'Грусть': sad,
        'Удивление': surprise,
        'Нейтральность': neutral,
        'Преобладающая эмоция': top_emotion,
        'Эмоциональный оттенок': emotion_shade,
        'Вовлеченность': engagement
    }
    os.remove(video_path)
    shutil.rmtree('../ademotions/output')
    return analyze_result



def top(angry, disgust, fear, happy, sad, surprise, neutral):
    emotions = {
    'Злость': angry,
    'Отвращение': disgust,
    'Страх': fear,
    'Счастье': happy,
    'Грусть': sad,
    'Удивление': surprise,
    'Нейтральность': neutral
    }
    max_value = max(emotions, key=emotions.get)
    return max_value

def shade(angry, disgust, fear, happy, sad, surprise, neutral):
    positive_emotions = [happy, surprise]
    negative_emotions = [angry, disgust, fear, sad]
    positive_value = sum(positive_emotions)
    negative_value = sum(negative_emotions)
    if ((positive_value-negative_value)>0):
        return 'Позитивный'
    else:
        return 'Негативный'

def to_percentage(angry, disgust, fear, happy, sad, surprise, neutral=0):
    emotions = [angry, disgust, fear, happy, sad, surprise, neutral]
    total = sum(emotions)
    percent_emotions = [round((emotion/total)*100) for emotion in emotions]
    return percent_emotions

def is_engagement(percent_emotions):
    max_value = max(percent_emotions)
    if (int(max_value)>5):
        return 1
    else:
        return 0
