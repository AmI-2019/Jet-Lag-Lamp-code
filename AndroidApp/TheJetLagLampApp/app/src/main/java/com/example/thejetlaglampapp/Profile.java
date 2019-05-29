package com.example.thejetlaglampapp;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.example.thejetlaglampapp.com.example.thejetlaglampapp.firebase.Database;
import com.example.thejetlaglampapp.com.example.thejetlaglampapp.firebase.ModifyProfile;
import com.example.thejetlaglampapp.com.example.thejetlaglampapp.firebase.User;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.DocumentSnapshot;

public class Profile extends AppCompatActivity {

    private static final String TAG = Profile.class.getSimpleName();
    Button btn_modifyProfile;
    private String mail;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_profile);

        mail = FirebaseAuth.getInstance().getCurrentUser().getEmail();
        btn_modifyProfile = findViewById(R.id.btn_modifyProfile);

        new AsyncTask<Void, Void, Boolean>() {

            TextView textView_Name = (TextView) findViewById(R.id.textView_Name);
            TextView textView_Surname = (TextView) findViewById(R.id.textView_Surname);
            TextView textView_email = (TextView) findViewById(R.id.textView_email);
            TextView textView_age = (TextView) findViewById(R.id.textView_age);
            TextView textView_homeAddress = (TextView) findViewById(R.id.textView_homeAddress);
            TextView textView_avgSleepingTime = (TextView) findViewById(R.id.textView_avgSleepingTime);
            TextView textView_avgDeepSleepTime = (TextView) findViewById(R.id.textView_avgDeepSleepTime);
            TextView textView_avgLightSleepTime = (TextView) findViewById(R.id.textView_avgLightSleepTime);


            @Override
            protected Boolean doInBackground(Void... voids) {

                DocumentReference docRef = Database.getFirestoreInstance().collection("Users").document(mail);

                docRef.get().addOnCompleteListener(new OnCompleteListener<DocumentSnapshot>() {
                    @Override
                    public void onComplete(@NonNull Task<DocumentSnapshot> task) {

                        if (task.isSuccessful()) {
                            DocumentSnapshot document = task.getResult();
                            if (document.exists()) {
                                Log.d(TAG, "DocumentSnapshot data: " + document.getData());
                                User user = document.toObject(User.class);
                                System.out.println(user);

                                textView_Name.setText("Name: " + user.getName());
                                textView_Surname.setText("Surname: " + user.getSurname());
                                textView_email.setText("Email: " + user.getEmail());
                                textView_age.setText("Age: " + Integer.toString(user.getAge()));
                                textView_homeAddress.setText("Home address: " + user.getHome_address());
                                textView_avgSleepingTime.setText("AVG sleeping time (min): " + Integer.toString(user.getAvgSleepingTimeMin()));
                                textView_avgDeepSleepTime.setText("AVG deep sleep time (min): " + Integer.toString(user.getAvgDeepSleepTimeMin()));
                                textView_avgLightSleepTime.setText("AVG light sleep time (min): " + Integer.toString(user.getAvgLightSleepTimeMin()));
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

        btn_modifyProfile.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openModifyActivity();
            }
        });
    }


    private void openModifyActivity() {
        Intent intent_ModifyProfileActivity = new Intent(Profile.this, ModifyProfile.class);
        startActivity(intent_ModifyProfileActivity);
    }

}
