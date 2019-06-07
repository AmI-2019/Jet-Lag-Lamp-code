package com.example.thejetlaglampapp.com.example.thejetlaglampapp.firebase;

import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.example.thejetlaglampapp.R;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.firestore.DocumentReference;

public class ModifyProfile extends AppCompatActivity {
    private static final String TAG = ModifyProfile.class.getSimpleName();
    Button btn_UpdateProfile;
    private String mail;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_modify_profile);
        btn_UpdateProfile = findViewById(R.id.btn_UpdateProfile);
        mail = FirebaseAuth.getInstance().getCurrentUser().getEmail();
        btn_UpdateProfile.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                UpdateProfile();
            }
        });
    }


    private void UpdateProfile() {


        EditText editText_Name = findViewById(R.id.editText_Name);
        EditText editText_Surname = findViewById(R.id.editText_Surname);
        EditText editText_email = findViewById(R.id.editText_email);
        EditText editText_age = findViewById(R.id.editText_age);
        EditText editText_homeAddress = findViewById(R.id.editText_homeAddress);
        EditText editText_typicalBedTime = findViewById(R.id.editText_typicalBedTime);
        EditText editText_typicalWakeUpTime = findViewById(R.id.editText_typicalWakeUpTime);


        DocumentReference docRef = Database.getFirestoreInstance().collection("Users").document(mail);
        docRef.update("name", editText_Name.getText().toString(),
                "surname", editText_Surname.getText().toString(),
                "email", editText_email.getText().toString(),
                "age", Integer.parseInt(editText_age.getText().toString()),
                "home_address", editText_homeAddress.getText().toString(),
                "typicalBedTime", editText_typicalBedTime.getText().toString(),
                "typicalWakeUpTime", editText_typicalWakeUpTime.getText().toString()

        )
                .addOnSuccessListener(new OnSuccessListener<Void>() {
                    @Override
                    public void onSuccess(Void aVoid) {
                        Log.d(TAG, "DocumentSnapshot successfully updated!");
                        Toast.makeText(getApplicationContext(), "Profile updated", Toast.LENGTH_SHORT).show();
                    }
                })
                .addOnFailureListener(new OnFailureListener() {
                    @Override
                    public void onFailure(@NonNull Exception e) {
                        Log.d(TAG, "Error updating document", e);
                    }
                })
        ;
    }
}



