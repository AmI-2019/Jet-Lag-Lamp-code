package com.example.thejetlaglampapp;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.provider.CalendarContract;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.example.thejetlaglampapp.com.example.thejetlaglampapp.firebase.Database;
import com.example.thejetlaglampapp.com.example.thejetlaglampapp.firebase.User;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.Timestamp;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.DocumentSnapshot;

import java.util.Calendar;
import java.util.Date;


public class DailyPlan extends AppCompatActivity {
    Button btn_OpenCalendar;
    Button btn_AddSuggestions;
    TextView textView_todaySleepSchedule;

    private static final String TAG = Profile.class.getSimpleName();
    String mail = FirebaseAuth.getInstance().getCurrentUser().getEmail();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_daily_plan);

        btn_OpenCalendar=findViewById(R.id.btn_OpernCalendar);
        btn_AddSuggestions=findViewById(R.id.btn_AddSuggestions);
        textView_todaySleepSchedule=findViewById(R.id.textView_todaySleepSchedule);


        btn_OpenCalendar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openCalendar();
            }
        });
        btn_AddSuggestions.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(addSuggestionsToCalendar()){

                }

            }
        });
        new AsyncTask<Void, Void, Boolean>() {

            @Override
            protected Boolean doInBackground(Void... voids) {

                final DocumentReference docRef = Database.getFirestoreInstance().collection("Users").document(mail);

                docRef.get().addOnCompleteListener(new OnCompleteListener<DocumentSnapshot>() {
                    @Override
                    public void onComplete(@NonNull Task<DocumentSnapshot> task) {

                        if (task.isSuccessful()) {
                            DocumentSnapshot document = task.getResult();
                            if (document.exists()) {
                                User user = document.toObject(User.class);
                                System.out.println(user);
                                textView_todaySleepSchedule.setText("Based on your sleeping habit today you should go to sleep at: \t"+ user.getTodaySleepSchedule()+"\n tomorrow you should wake up at: \t"+user.getTomorrowWakeUpSchedule());
                            } else {
                                Log.d(TAG, "No such document");
                            }
                        } else {
                            Log.d(TAG, "get failed with ", task.getException());
                        }

                    }


                });
                return true;

            }

        }.execute();

    }


    private boolean addSuggestionsToCalendar() {

        new AsyncTask<Void, Void, Boolean>() {

            @Override
            protected Boolean doInBackground(Void... voids) {


                final DocumentReference docRef = Database.getFirestoreInstance().collection("Users").document(mail)
                        .collection("DailyPlan").document("suggestions");

                docRef.get().addOnCompleteListener(new OnCompleteListener<DocumentSnapshot>() {
                    @Override
                    public void onComplete(@NonNull Task<DocumentSnapshot> task) {

                        if (task.isSuccessful()) {
                            DocumentSnapshot document = task.getResult();
                            if (document.exists()) {
                                Log.d(TAG, "DocumentSnapshot data: " + document.getData());
                                Timestamp ts1 = document.getTimestamp("str1");
                                //Timestamp ts2 = document.getTimestamp("str2");
                                Timestamp ts1_e = document.getTimestamp("end1");
                                //Timestamp ts2_e = document.getTimestamp("end2");
                                Date dt1= ts1.toDate();
                                //Date dt2= ts2.toDate();
                                Date dt1_e= ts1_e.toDate();
                                //Date dt2_e= ts2_e.toDate();
                                //First break
                                Calendar beginTime1 = Calendar.getInstance();
                                beginTime1.setTime(dt1);
                                Calendar endTime1 = Calendar.getInstance();
                                endTime1.setTime(dt1_e);
                                Intent intent_calendar1 = new Intent(Intent.ACTION_INSERT)
                                        .setData(CalendarContract.Events.CONTENT_URI)
                                        .putExtra(CalendarContract.EXTRA_EVENT_BEGIN_TIME, beginTime1.getTimeInMillis())
                                        .putExtra(CalendarContract.EXTRA_EVENT_END_TIME, endTime1.getTimeInMillis())
                                        .putExtra(CalendarContract.Events.TITLE, "Take time to relax")
                                        .putExtra(CalendarContract.Events.DESCRIPTION, "TheJetLagLampApp")
                                        .putExtra(CalendarContract.Events.AVAILABILITY, CalendarContract.Events.AVAILABILITY_BUSY);
                                startActivity(intent_calendar1);


                            } else {
                                Log.d(TAG, "No such document");
                            }
                        } else {
                            Log.d(TAG, "get failed with ", task.getException());
                        }

                    }


                });
                return true;

            }

        }.execute();

        return true;
    }

    private void openCalendar() {
            Intent intent_Calendar = new Intent(DailyPlan.this, CalendarApp.class);
            startActivity(intent_Calendar);
    }
}
