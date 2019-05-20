package com.example.thejetlaglampapp.com.example.thejetlaglampapp.firebase;

import android.support.annotation.NonNull;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.firestore.DocumentSnapshot;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.FirebaseFirestoreSettings;
/*Per trovare la mail dell'utente loggato
FirebaseAuth.getInstance().getCurrentUser().....
* */
public class Database {

    private static FirebaseFirestore INSTANCE;

    public static FirebaseFirestore getFirestoreInstance(){
        if(INSTANCE == null){
            INSTANCE = FirebaseFirestore.getInstance();
            FirebaseFirestoreSettings settings = new FirebaseFirestoreSettings.Builder()
                    .setTimestampsInSnapshotsEnabled(true)
                    .build();
            INSTANCE.setFirestoreSettings(settings);
        }
        return INSTANCE;
    }


    public static void getUser(String mail){
        getFirestoreInstance().collection("Users").document(mail).get().addOnCompleteListener(new OnCompleteListener<DocumentSnapshot>() {
            @Override
            public void onComplete(@NonNull Task<DocumentSnapshot> task) {
                if(task.isSuccessful()){
                    User u = task.getResult().toObject(User.class);
                }
            }
        });
    }
}
