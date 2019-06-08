package com.example.thejetlaglampapp;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Switch;
import android.widget.Toast;

import com.example.thejetlaglampapp.com.example.thejetlaglampapp.firebase.Database;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.firestore.DocumentReference;

public class TravelInfo extends AppCompatActivity {
    Button btn_UpdateAdditionalInfo;
    Switch switch_enableSystem;
    EditText editText_lastCountry;
    private String mail;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_travel_info);

        btn_UpdateAdditionalInfo=findViewById(R.id.btn_UpdateAdditionalInfo);
        switch_enableSystem=findViewById(R.id.switch_enableSystem);
        editText_lastCountry=findViewById(R.id.editText_lastCountry);

        mail = FirebaseAuth.getInstance().getCurrentUser().getEmail();
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
