package com.example.thejetlaglampapp;

import android.Manifest;
import android.content.BroadcastReceiver;
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

import static android.content.Context.LOCATION_SERVICE;

public class WifiCheck extends BroadcastReceiver {
    String mail;
    @Override
    public void onReceive(Context context, Intent intent) {
        boolean inside=insideHotelNet(context);
        if(FirebaseAuth.getInstance().getCurrentUser()==null){
            mail="test";
        }
        else {
            mail= FirebaseAuth.getInstance().getCurrentUser().getEmail();
        }

        DocumentReference docRef = Database.getFirestoreInstance().collection("Users").document(mail);

        if (inside){

            Location locationGPS=getLastKnownLocation(context);
            Toast toast= Toast.makeText(context.getApplicationContext(),"Welcome, the rooms of this hotel are \n equiped with the JetLagLamp® system!",Toast.LENGTH_LONG);
            toast.show();

            docRef.update("hotel_address",String.valueOf(locationGPS.getLatitude())+","+ String.valueOf(locationGPS.getLongitude()),
                    "insideHotel",true);

        }
        else{
            docRef.update("insideHotel",false);
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
    private boolean insideHotelNet(Context context){
        String wifiName=getWifiName(context.getApplicationContext());
        if (wifiName!=null){
            if ( wifiName.contains("eduroam")){
                return true;
            }
            return false;
        }
        else {
            return false;
        }

    }
    private Location getLastKnownLocation(Context context){
        if( ActivityCompat.checkSelfPermission( context, Manifest.permission.ACCESS_FINE_LOCATION ) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission( context, Manifest.permission.ACCESS_COARSE_LOCATION ) != PackageManager.PERMISSION_GRANTED ){
            return null;
        }
        LocationManager locationManager =
                (LocationManager) context.getSystemService( LOCATION_SERVICE );
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

}
