package com.example.thejetlaglampapp;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import com.example.thejetlaglampapp.com.example.thejetlaglampapp.firebase.Database;
import com.example.thejetlaglampapp.com.example.thejetlaglampapp.firebase.Event;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.firestore.CollectionReference;
import com.google.firebase.firestore.DocumentReference;

public class newEventOnCalendar extends AppCompatActivity {
    EditText title,startTime,endTime;
    Button addButton;
    String mail;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_new_event_on_calendar);

        mail = FirebaseAuth.getInstance().getCurrentUser().getEmail();

        title=findViewById(R.id.editText_eventTitle);
        startTime=findViewById(R.id.editText_startTime);
        endTime=findViewById(R.id.editText_endTime);
        addButton=findViewById(R.id.btn_AddNewEventOnCalendar);


        addButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                CollectionReference collRef =Database
                        .getFirestoreInstance()
                        .collection("Users")
                        .document(mail)
                        .collection("events");

                Event event=new Event(title.getText().toString(),startTime.getText().toString(),endTime.getText().toString());

                collRef.add(event).addOnCompleteListener(new OnCompleteListener<DocumentReference>() {
                    @Override
                    public void onComplete(@NonNull Task<DocumentReference> task) {
                        openCalendar();
                    }
                });
            }
        });


    }
    private void openCalendar() {
        Intent intent_Calendar = new Intent(newEventOnCalendar.this, CalendarApp.class);
        startActivity(intent_Calendar);
    }
}
