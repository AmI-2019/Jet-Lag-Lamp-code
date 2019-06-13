package com.example.thejetlaglampapp;

import android.os.AsyncTask;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Switch;
import android.widget.Toast;

import com.example.thejetlaglampapp.com.example.thejetlaglampapp.firebase.Database;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.firestore.DocumentReference;
import com.google.firebase.firestore.DocumentSnapshot;

public class TravelInfo extends AppCompatActivity {
    Button btn_UpdateAdditionalInfo;
    Switch switch_enableSystem;
    EditText editText_lastCountry,editText_days;
    private String mail;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_travel_info);

        btn_UpdateAdditionalInfo=findViewById(R.id.btn_UpdateAdditionalInfo);
        switch_enableSystem=findViewById(R.id.switch_enableSystem);
        editText_lastCountry=findViewById(R.id.editText_lastCountry);
        editText_days=findViewById(R.id.editText_days);

        mail = FirebaseAuth.getInstance().getCurrentUser().getEmail();
        new AsyncTask<Void, Void, Boolean>() {
            //FOUND_ON https://stackoverflow.com/questions/50035752/how-to-get-list-of-documents-from-a-collection-in-firestore-android
                @Override
                protected Boolean doInBackground(Void... voids) {
                    Database.getFirestoreInstance()
                            .collection("Users")
                            .document(mail)
                            .get()
                            .addOnCompleteListener(new OnCompleteListener<DocumentSnapshot>() {
                                @Override
                                public void onComplete(@NonNull Task<DocumentSnapshot> task) {
                                    if (task.isSuccessful()) {
                                        switch_enableSystem.setChecked(task.getResult().getBoolean("enableSystem"));
                                        editText_lastCountry.setText(task.getResult().getString("lastCountry"));
                                        editText_days.setText(task.getResult().getString("trip_duration"));
                                    }
                                }
                            });
                    return true;
                }

            }.execute();

        btn_UpdateAdditionalInfo.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                UpdateAdditionalInfo();
            }
        });

    }
    private void UpdateAdditionalInfo() {

        EditText editText_days = findViewById(R.id.editText_days);
        DocumentReference docRef = Database.getFirestoreInstance().collection("Users").document(mail);
        docRef.update("trip_duration",editText_days.getText().toString(),
                "enableSystem",switch_enableSystem.isChecked(),
                "lastCountry",editText_lastCountry.getText().toString())
                .addOnSuccessListener(new OnSuccessListener<Void>() {
                    @Override
                    public void onSuccess(Void aVoid) {
                        Toast.makeText(getApplicationContext(), "Info updated", Toast.LENGTH_SHORT).show();
                    }
                })
        ;
    }
}
