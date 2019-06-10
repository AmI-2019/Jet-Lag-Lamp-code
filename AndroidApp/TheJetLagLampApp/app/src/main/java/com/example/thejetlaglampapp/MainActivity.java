package com.example.thejetlaglampapp;

import android.Manifest;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.location.LocationListener;
import android.location.LocationManager;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.support.annotation.RequiresApi;
import android.support.v4.app.ActivityCompat;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;

import com.google.firebase.auth.FirebaseAuth;


public class MainActivity extends AppCompatActivity {

        Button btn_SingIn;
        Button btn_DailyPlan;
        Button btn_Hotels;
        Button btn_TravelInfo;
        Button btn_Website;
        Button btn_AboutUs;
        Button btn_ViewProfile;
        private String mail;
        protected LocationManager locationManager;
        protected LocationListener locationListener;

    private static final String[] GPS_PERM = {
            Manifest.permission.ACCESS_FINE_LOCATION
    };
    private static final String[] READCALENDAR_PERM = {
            Manifest.permission.READ_CALENDAR
    };
    private static final String[] WRITECALENDAR_PERM = {
            Manifest.permission.WRITE_CALENDAR
    };


    @RequiresApi(api = Build.VERSION_CODES.M)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        //Permissions
        if(ActivityCompat.checkSelfPermission(getApplicationContext(), Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED){
            requestPermissions(GPS_PERM,1010);
        }
        if(ActivityCompat.checkSelfPermission(getApplicationContext(), Manifest.permission.READ_CALENDAR) != PackageManager.PERMISSION_GRANTED){
            requestPermissions(READCALENDAR_PERM,1001);
        }
        if(ActivityCompat.checkSelfPermission(getApplicationContext(), Manifest.permission.WRITE_CALENDAR) != PackageManager.PERMISSION_GRANTED){
            requestPermissions(WRITECALENDAR_PERM,1011);
        }


        mail=FirebaseAuth.getInstance().getCurrentUser().getEmail();

        if (mail==null){
            openSingInActivity();
            mail=FirebaseAuth.getInstance().getCurrentUser().getEmail();
        }

        setContentView(R.layout.activity_main);
        // Button definitions
        btn_SingIn=findViewById(R.id.btn_SingIn);
        btn_Hotels=findViewById(R.id.btn_Hotels);
        btn_DailyPlan=findViewById(R.id.btn_DailyPlan);
        btn_TravelInfo =findViewById(R.id.btn_TravelInfo);
        btn_Website=findViewById(R.id.btn_Website);
        btn_AboutUs=findViewById(R.id.btn_AboutUs);
        btn_ViewProfile=findViewById(R.id.btn_ViewProfile);


        //scheduleJob();

        //OnClickListener init
        btn_SingIn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openSingInActivity();
            }
        });
        btn_Hotels.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openHotelsActivity();
            }
        });
        btn_ViewProfile.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openViewProfileActivity();
            }
        });
        btn_AboutUs.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openAboutUsActivity();
            }
        });
        btn_Website.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openWebsiteActivity();
            }
        });
        btn_DailyPlan.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openDailyPlanActivity();
            }
        });
        btn_TravelInfo.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openTravelInfoActivity();
            }
        });

    }

    //------------------------------------------------------------------------------------------
   /* public void scheduleJob(){
        ComponentName componentName = new ComponentName(this, MyJobService.class);
        JobInfo info = new JobInfo.Builder(123, componentName)
                .setRequiredNetworkType(JobInfo.NETWORK_TYPE_ANY)
                .setPersisted(true)
                .setPeriodic(15 * 60 * 1000)
                .build();

        JobScheduler scheduler = (JobScheduler) getSystemService(JOB_SCHEDULER_SERVICE);
        int resultCode = scheduler.schedule(info);
        if (resultCode == JobScheduler.RESULT_SUCCESS) {
            Toast.makeText(this, "Job schedulato con successo", Toast.LENGTH_LONG).show();
        }
    }

    public void cancelJob() {
        JobScheduler scheduler = (JobScheduler) getSystemService(JOB_SCHEDULER_SERVICE);
        scheduler.cancel(123);
    }*/
    //------------------------------------------------------------------------------------------


    //Open function definitions
    private void openDailyPlanActivity() {
        Intent intent_DailyPlan=new Intent(MainActivity.this,DailyPlan.class);
        startActivity(intent_DailyPlan);
    }
    private void openSingInActivity(){
            Intent intent_SigIn=new Intent(MainActivity.this, GoogleSingInActivity.class);
            startActivity(intent_SigIn);
    }
    private void openViewProfileActivity() {
        Intent intent_ViewProfile = new Intent(MainActivity.this, Profile.class);
        startActivity(intent_ViewProfile);
    }
    private void openAboutUsActivity() {
        Intent intent_AboutUs = new Intent(MainActivity.this, AboutUs.class);
        startActivity(intent_AboutUs);
    }
    private void openWebsiteActivity() {
        Uri uri = Uri.parse("https://ami-2019.github.io/Jet-Lag-Lamp/"); // missing 'http://' will cause crashed
        Intent intent_Website = new Intent(Intent.ACTION_VIEW, uri);
        startActivity(intent_Website);
    }
    private void openHotelsActivity() {
        Intent intent_Hotels = new Intent(MainActivity.this, Hotels.class);
        startActivity(intent_Hotels);
    }
    private void openTravelInfoActivity() {
        Intent intent_TravelInfo = new Intent(MainActivity.this, TravelInfo.class);
        startActivity(intent_TravelInfo);
    }



}
