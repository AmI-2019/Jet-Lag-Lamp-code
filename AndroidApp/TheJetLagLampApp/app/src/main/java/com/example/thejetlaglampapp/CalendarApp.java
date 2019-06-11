package com.example.thejetlaglampapp;

import android.os.AsyncTask;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.ProgressBar;
import android.widget.Toast;

import com.example.thejetlaglampapp.com.example.thejetlaglampapp.firebase.Database;
import com.example.thejetlaglampapp.com.example.thejetlaglampapp.firebase.Event;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.firestore.CollectionReference;
import com.google.firebase.firestore.DocumentSnapshot;

import java.util.ArrayList;
import java.util.List;

public class CalendarApp extends AppCompatActivity {
    private static final String TAG = Profile.class.getSimpleName();
    String mail;
    ListView ListViewCalendar;
    ProgressBar pb;

    private ArrayList<String> events=new ArrayList<String>();
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_calendarapp);

        ListViewCalendar =findViewById(R.id.calendar);
        pb=findViewById(R.id.progress_bar);

        pb.setVisibility(View.VISIBLE);

        mail= FirebaseAuth.getInstance().getCurrentUser().getEmail();


        //fill the list view with the task list
        new AsyncTask<Void, Void, List<String>>() {

            @Override
            protected List<String> doInBackground(Void... voids) {

                CollectionReference collRef = Database.getFirestoreInstance().collection("Users").document(mail).collection("events");
                for (int i=1;i<=collRef.get().getResult().size();i++){ //Scnsiono tutti i documenti all'interno della collection
                    collRef.document(Integer.toString(i)).get().addOnCompleteListener(new OnCompleteListener<DocumentSnapshot>() {
                        @Override
                        public void onComplete(@NonNull Task<DocumentSnapshot> task) {

                            if (task.isSuccessful()) {
                                DocumentSnapshot document = task.getResult();
                                if (document.exists()) {
                                    Log.d(TAG, "DocumentSnapshot data: " + document.getData());
                                    Event event_firebase = document.toObject(Event.class);
                                    events.add(event_firebase.toString());
                                } else {
                                    Log.d(TAG, "No such document");
                                }
                            } else {
                                Log.d(TAG, "get failed with ", task.getException());
                            }

                        }
                    });
                }

                return events;
            }
            @Override
            protected void onPostExecute(List<String> events) {
                if(events != null) {
                    ArrayAdapter adapter = new ArrayAdapter(getApplicationContext(), android.R.layout.simple_list_item_2, events);
                    ListViewCalendar.setAdapter(adapter);
                    Toast toast = Toast.makeText(getApplicationContext(), "layoutcompleated", Toast.LENGTH_LONG);
                    pb.setVisibility(View.GONE);
                    toast.show();
                }
                else{
                    Toast toast = Toast.makeText(getApplicationContext(), "OOOOPS, something goes wrong!", Toast.LENGTH_LONG);
                    toast.show();
                }
            }
        }.execute();

    }
}
