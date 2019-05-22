package com.example.thejetlaglampapp.com.example.thejetlaglampapp.firebase;

import com.google.firebase.firestore.GeoPoint;

public class User {

    String name;
    String surname;
    Sleep_info AVG_sleep;
    Integer age;
    GeoPoint home_address;
    GeoPoint hotel_location;
    Integer white_noise_preference;

    public User(String name, String surname, Sleep_info AVG_sleep, Integer age, GeoPoint home_address, GeoPoint hotel_location, Integer white_noise_preference) {
        this.name = name;
        this.surname = surname;
        this.AVG_sleep = AVG_sleep;
        this.age = age;
        this.home_address = home_address;
        this.hotel_location = hotel_location;
        this.white_noise_preference = white_noise_preference;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }

    public Sleep_info getAVG_sleep() {
        return AVG_sleep;
    }

    public void setAVG_sleep(Sleep_info AVG_sleep) {
        this.AVG_sleep = AVG_sleep;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    public GeoPoint getHome_address() {
        return home_address;
    }

    public void setHome_address(GeoPoint home_address) {
        this.home_address = home_address;
    }

    public GeoPoint getHotel_location() {
        return hotel_location;
    }

    public void setHotel_location(GeoPoint hotel_location) {
        this.hotel_location = hotel_location;
    }

    public Integer getWhite_noise_preference() {
        return white_noise_preference;
    }

    public void setWhite_noise_preference(Integer white_noise_preference) {
        this.white_noise_preference = white_noise_preference;
    }
};
