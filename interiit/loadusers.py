from django.db import models
from django.contrib.auth.models import User
from interiit.models import Profile, Details
import random
import os
import csv

iit_list = ['IIT MADRAS']

# iit_list = ['IIT MADRAS','IIT KHARAGPUR','IIT BOMBAY','IIT KANPUR','IIT DELHI','IIT GUWAHATI','IIT ROORKEE','IIT BHUBANESWAR','IIT GANDHINAGAR','IIT HYDERABAD','IIT JODHPUR','IIT PATNA','IIT ROPAR','IIT INDORE','IIT MANDI','IIT VARANASI']
sports_list = ['Staff','Athletics M','Athletics F','Badminton','Basketball','Cricket','FootBall','Hockey','Squash','Table Tennis','Tennis','Volleyball','Weightlifting',]
sports_events = ['100 M','200 M','400 M', '800 M', '1500 M', '5000 M', '110 M Hurdles', '400 M Hurdles', 'High Jump', 'Long Jump', 'Triple Jump', 'Pole Vault', 'Shot Put', 'Discuss Throw', 'Javelin Throw', 'Hammer Throw', '4x100 M Relay', '4x400 M Relay']    
sports_events_f = ['100 M','200 M','400 M', '800 M','1500 M', 'High Jump', 'Long Jump', 'Shot Put', 'Discuss Throw', '4x100 M Relay', '4x400 M Relay']
participant_type = ['Participant 1 ','Participant 2','Reserve']
participant_type2 = ['Participant 1 ','Participant 2','Participant 3','Participant 4','Reserve 1','Reserve 2']
weight_event = ['Upto 56 kg','Upto 62 kg','Upto 69 kg','Upto 77 kg','Above 77 kg']



final_id=[]
for i in iit_list:

    for j in sports_list:
        password = i + str(random.randint(100,999))
        username = str(i) + '_' + str(j)
        temp={}
        temp['ID'] = username
        temp['Password'] = password
        final_id.append(temp)
        user = User.objects.create_user(username=username,password= password)
        p_details = Details(user=user,sport=str(j),college=str(i))
        p_details.save()
        if j == 'Athletics M':
            for k in sports_events:
                if k == '4x100 M Relay' or k == '4x400 M Relay':
                    part_type = participant_type2
                else :
                    part_type = participant_type
                for l in part_type :
                    p_profile = Profile(user=user,event=k,participant_type=l,gender='M')
                    p_profile.save()
        if j == 'Athletics M':
            for k in sports_events_f:
                if k == '4x100 M Relay' or k == '4x400 M Relay':
                    part_type = participant_type2
                else :
                    part_type = participant_type
                for l in part_type :
                    p_profile = Profile(user=user,event=k,participant_type=l,gender='F')
                    p_profile.save()
        if j == 'Weightlifting':
            for k in weight_event:
                for l in participant_type :
                    p_profile = Profile(user=user,event=k,participant_type=l)
                    p_profile.save()
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname('__file__'),''))
answer_file_location = os.path.join(PROJECT_PATH, 'login_details.csv')
with open(answer_file_location, 'wb') as csv_file:
    writer = csv.DictWriter(csv_file, ['ID', 'Password'])
    writer.writeheader()
    for item in final_id:
        writer.writerow(item)
