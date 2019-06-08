package com.example.thejetlaglampapp;

import android.Manifest;
import android.app.job.JobParameters;
import android.app.job.JobService;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationManager;
import android.net.NetworkInfo;
import android.net.wifi.WifiInfo;
import android.net.wifi.WifiManager;
import android.support.v4.app.ActivityCompat;
import android.widget.Toast;

import com.example.thejetlaglampapp.com.example.thejetlaglampapp.firebase.Database;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.firestore.DocumentReference;

import java.util.List;

public class MyJobService extends JobService {
    String mail;

    public MyJobService() {
    }
//--------------------------------------------------------------------------------------------------
    @Override
    public boolean onStartJob(JobParameters params) {
        /*
         * True - if your service needs to process
         * the work (on a separate thread).
         * False - if there's no more work to be done for this job.
         */
        doBackgroundWork(params);

        return true;
    }

//--------------------------------------------------------------------------------------------------
    @Override
    public boolean onStopJob(JobParameters params) {
        return true;
    }
//--------------------------------------------------------------------------------------------------


    private boolean checkWifiOnAndConnected() {
        WifiManager wifiMgr = (WifiManager) getApplicationContext().getSystemService(Context.WIFI_SERVICE);

        if (wifiMgr.isWifiEnabled()) { // Wi-Fi adapter is ON

            WifiInfo wifiInfo = wifiMgr.getConnectionInfo();

            if( wifiInfo.getNetworkId() == -1 ){
                return false; // Not connected to an access point
            }
            return true; // Connected to an access point
        }
        else {
            return false; // Wi-Fi adapter is OFF
        }
    }
    public String getWifiName(Context context) {
        WifiManager manager = (WifiManager) context.getApplicationContext().getSystemService(Context.WIFI_SERVICE);
        if (manager.isWifiEnabled()) {
            WifiInfo wifiInfo = manager.getConnectionInfo();
            if (wifiInfo != null) {
                NetworkInfo.DetailedState state = WifiInfo.getDetailedStateOf(wifiInfo.getSupplicantState());
                if (state == NetworkInfo.DetailedState.CONNECTED || state == NetworkInfo.DetailedState.OBTAINING_IPADDR) {
                    return wifiInfo.getSSID();
                }
            }
        }
        return null;
    }
    private boolean insideHotelNet(){
        String wifiName=getWifiName(getApplicationContext());
        if (wifiName!=null){
            if ( wifiName.contains("Vodafone5GHz-35017716")){
                return true;
            }
            return false;
        }
        else {
            return false;
        }

    }


    private void doBackgroundWork(final JobParameters params) {
        mail= FirebaseAuth.getInstance().getCurrentUser().getEmail();
        if (mail==null){
            openSingInActivity();
            mail=FirebaseAuth.getInstance().getCurrentUser().getEmail();
        }
        System.out.println(getWifiName(getApplicationContext()));
        boolean condition=insideHotelNet();
            if (condition){
                Location locationGPS=getLastKnownLocation();
                Toast toast= Toast.makeText(getApplicationContext(),"Welcome, the rooms of this hotel are \n equiped with the JetLagLamp® system!",Toast.LENGTH_LONG);
                toast.show();

                DocumentReference docRef = Database.getFirestoreInstance().collection("Users").document(mail);

                docRef.update("hotel_address",String.valueOf(locationGPS.getLatitude())+","+ String.valueOf(locationGPS.getLongitude()),
                        "insideHotel",true);

            }
            else{
                DocumentReference docRef = Database.getFirestoreInstance().collection("Users").document(mail);

                docRef.update("insideHotel",false);
            }
    }
    private Location getLastKnownLocation(){
        if( ActivityCompat.checkSelfPermission( this, Manifest.permission.ACCESS_FINE_LOCATION ) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission( this, Manifest.permission.ACCESS_COARSE_LOCATION ) != PackageManager.PERMISSION_GRANTED ){
            return null;
        }
        LocationManager locationManager =
                (LocationManager) this.getSystemService( LOCATION_SERVICE );
        List<String> providers = locationManager.getProviders( true );
        Location bestLocation = null;
        for( String provider : providers ){
            Location l = locationManager.getLastKnownLocation( provider );
            if( l == null ){
                continue;
            }
            if( bestLocation == null || l.getAccuracy() < bestLocation.getAccuracy() ){
                bestLocation = l; // Found best last known location;
            }
        }
        return bestLocation;
    }

    private void openSingInActivity(){
        Intent intent_SigIn=new Intent(MyJobService.this, GoogleSingInActivity.class);
        startActivity(intent_SigIn);
    }

}