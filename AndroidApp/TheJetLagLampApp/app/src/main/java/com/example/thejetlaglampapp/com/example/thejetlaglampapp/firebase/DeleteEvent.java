package com.example.thejetlaglampapp.com.example.thejetlaglampapp.firebase;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.example.thejetlaglampapp.CalendarApp;
import com.example.thejetlaglampapp.R;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.firestore.CollectionReference;
import com.google.firebase.firestore.DocumentSnapshot;
import com.google.firebase.firestore.QuerySnapshot;

import java.util.Iterator;
import java.util.List;

public class DeleteEvent extends AppCompatActivity {
    private static final String TAG = DeleteEvent.class.getSimpleName();
    private String mail;
    Button btn_delete;
    EditText eventTitle;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_delete_event);
        mail = FirebaseAuth.getInstance().getCurrentUser().getEmail();
        eventTitle = findViewById(R.id.editText_TitleDelEvent);
        btn_delete = findViewById(R.id.btn_DeleteEvent);


        //Delete event using title
        btn_delete.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                new AsyncTask<Void, Void, Boolean>() {
                    //FOUND_ON https://stackoverflow.com/questions/50035752/how-to-get-list-of-documents-from-a-collection-in-firestore-android
                    @Override
                    protected Boolean doInBackground(Void... voids) {


                        final CollectionReference collRef = Database.getFirestoreInstance()
                                .collection("Users")
                                .document(mail)
                                .collection("events");
                        collRef.get()
                                .addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
                                    @Override
                                    public void onComplete(@NonNull Task<QuerySnapshot> task) {
                                        if (task.isSuccessful()) {
                                            List<DocumentSnapshot> documents = task.getResult().getDocuments();
                                            Iterator<DocumentSnapshot> itDocSnapshot = documents.iterator();
                                            while (itDocSnapshot.hasNext()) { //Scansiono tutti i documenti all'interno della collection
                                                DocumentSnapshot document = itDocSnapshot.next();
                                                if (document.getString("title").contains(eventTitle.getText().toString())) {

                                                    collRef.document(document.getId()).delete();
                                                    Toast toast = Toast.makeText(getApplicationContext(), "Event deleted", Toast.LENGTH_LONG);
                                                    toast.show();
                                                } else {
                                                    Log.d(TAG, "No such document");
                                                }
                                            }

                                        } else {
                                            Log.d(TAG, "get failed with ", task.getException());
                                        }
                                        openCalendar();
                                    }
                                });


                        return true;
                    }

                }.execute();
            }
        });

    }
    private void openCalendar() {
        Intent intent_Calendar = new Intent(DeleteEvent.this, CalendarApp.class);
        startActivity(intent_Calendar);
    }
}

