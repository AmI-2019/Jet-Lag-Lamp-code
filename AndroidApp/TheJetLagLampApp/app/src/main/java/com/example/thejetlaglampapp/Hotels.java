package com.example.thejetlaglampapp;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;

public class Hotels extends AppCompatActivity {
    Button btn_hotelWebsite;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_hotels);
        btn_hotelWebsite=findViewById(R.id.btn_hotelWebsite);

        btn_hotelWebsite.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openHotelWebsite();
            }
        });
    }
    private void openHotelWebsite() {
        Uri uri = Uri.parse("https://vincentgautier.github.io/Hotel-web-site/"); // missing 'http://' will cause crashed
        Intent intent_Website = new Intent(Intent.ACTION_VIEW, uri);
        startActivity(intent_Website);
    }
}
