package com.example.thejetlaglampapp;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ImageButton;
import android.widget.ListView;
import android.widget.ProgressBar;

import com.example.thejetlaglampapp.com.example.thejetlaglampapp.firebase.Database;
import com.example.thejetlaglampapp.com.example.thejetlaglampapp.firebase.DeleteEvent;
import com.example.thejetlaglampapp.com.example.thejetlaglampapp.firebase.Event;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.firestore.DocumentSnapshot;
import com.google.firebase.firestore.QuerySnapshot;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class CalendarApp extends AppCompatActivity {
    private static final String TAG = CalendarApp.class.getSimpleName();
    String mail;
    ListView ListViewCalendar;
    ProgressBar pb;
    ImageButton btn_AddCalendar_event;
    ImageButton btn_DelCalendar_event;
    private ArrayList<String> events=new ArrayList<String>();
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_calendarapp);

        ListViewCalendar =findViewById(R.id.calendar);
        pb=findViewById(R.id.progress_bar);
        btn_AddCalendar_event=findViewById(R.id.btn_AddCalendar_event);
        btn_DelCalendar_event=findViewById(R.id.btn_DelCalendar_event);
       // pb.setVisibility(View.VISIBLE);

        mail= FirebaseAuth.getInstance().getCurrentUser().getEmail();


        //fill the list view with the task list
        new AsyncTask<Void, Void, List<String>>() {
            //FOUND_ON https://stackoverflow.com/questions/50035752/how-to-get-list-of-documents-from-a-collection-in-firestore-android
            @Override
            protected List<String> doInBackground(Void... voids) {


                Database.getFirestoreInstance()
                        .collection("Users")
                        .document(mail)
                        .collection("events")
                        .get()
                        .addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
                            @Override
                            public void onComplete(@NonNull Task<QuerySnapshot> task) {
                                if (task.isSuccessful()) {
                                    List<DocumentSnapshot> documents = task.getResult().getDocuments();
                                    Iterator<DocumentSnapshot> itDocSnapshot=documents.iterator();
                                    while(itDocSnapshot.hasNext()) { //Scansiono tutti i documenti all'interno della collection
                                        DocumentSnapshot document = itDocSnapshot.next();
                                        if (document.exists()) {
                                            Log.d(TAG, "DocumentSnapshot data: " + document.getData());
                                            Event event_firebase = document.toObject(Event.class);
                                            events.add(event_firebase.toString());
                                        } else {
                                            Log.d(TAG, "No such document");
                                        }
                                    }
                                    //To be added... sorting events
                                    ArrayAdapter adapter = new ArrayAdapter(getApplicationContext(), android.R.layout.simple_list_item_1, events);
                                    try {
                                        ListViewCalendar.setAdapter(adapter);
                                    } catch(Throwable t){
                                        t.printStackTrace();
                                    }

                                } else {
                                    Log.d(TAG, "get failed with ", task.getException());
                                }
                            }
                        });




                return events;
            }

        }.execute();
        btn_AddCalendar_event.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openNewEventActivity();
            }
        });
        btn_DelCalendar_event.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openDeleteEvent();
            }
        });
    }
    void openNewEventActivity(){
        Intent intent_newEventOnCalendar = new Intent(CalendarApp.this, newEventOnCalendar.class);
        startActivity(intent_newEventOnCalendar);
    }
    void openDeleteEvent(){
        Intent intent_deleteEventOnCalendar = new Intent(CalendarApp.this, DeleteEvent.class);
        startActivity(intent_deleteEventOnCalendar);
    }
}
