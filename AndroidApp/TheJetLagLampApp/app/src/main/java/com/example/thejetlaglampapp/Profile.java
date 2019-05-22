package com.example.thejetlaglampapp;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;

import com.example.thejetlaglampapp.com.example.thejetlaglampapp.firebase.Database;
import com.example.thejetlaglampapp.com.example.thejetlaglampapp.firebase.User;

public class Profile extends AppCompatActivity {
    private static final String TAG = Profile.class.getSimpleName();
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_profile);
    }
    //String mail = FirebaseAuth.getInstance().getCurrentUser().getEmail();
    User user = Database.getUser("fabio.baldo17@gmail.com");

}
