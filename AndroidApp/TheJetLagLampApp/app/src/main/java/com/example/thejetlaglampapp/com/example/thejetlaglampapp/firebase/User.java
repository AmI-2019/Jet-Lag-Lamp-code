package com.example.thejetlaglampapp.com.example.thejetlaglampapp.firebase;

public class User {

    String name;
    String surname;
    Integer age;
    String email;
    String home_address;
    String hotel_address;
    Integer white_noise_preference;
    Integer avgSleepingTimeMin;
    Integer avgDeepSleepTimeMin;
    Integer avgLightSleepTimeMin;
    Integer avgAwakeTimeMin;
    Integer avgStepDay;

    public User() {

    }

    public User(String name, String surname, Integer age, String email, String home_address, String hotel_address, Integer white_noise_preference, Integer avgSleepingTimeMin, Integer avgDeepSleepTimeMin, Integer avgLightSleepTimeMin, Integer avgAwakeTimeMin, Integer avgStepDay) {
        this.name = name;
        this.surname = surname;
        this.age = age;
        this.email = email;
        this.home_address = home_address;
        this.hotel_address = hotel_address;
        this.white_noise_preference = white_noise_preference;
        this.avgSleepingTimeMin = avgSleepingTimeMin;
        this.avgDeepSleepTimeMin = avgDeepSleepTimeMin;
        this.avgLightSleepTimeMin = avgLightSleepTimeMin;
        this.avgAwakeTimeMin = avgAwakeTimeMin;
        this.avgStepDay = avgStepDay;
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

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getHome_address() {
        return home_address;
    }

    public void setHome_address(String home_address) {
        this.home_address = home_address;
    }

    public String getHotel_address() {
        return hotel_address;
    }

    public void setHotel_address(String hotel_address) {
        this.hotel_address = hotel_address;
    }

    public Integer getWhite_noise_preference() {
        return white_noise_preference;
    }

    public void setWhite_noise_preference(Integer white_noise_preference) {
        this.white_noise_preference = white_noise_preference;
    }

    public Integer getAvgSleepingTimeMin() {
        return avgSleepingTimeMin;
    }

    public void setAvgSleepingTimeMin(Integer avgSleepingTimeMin) {
        this.avgSleepingTimeMin = avgSleepingTimeMin;
    }

    public Integer getAvgDeepSleepTimeMin() {
        return avgDeepSleepTimeMin;
    }

    public void setAvgDeepSleepTimeMin(Integer avgDeepSleepTimeMin) {
        this.avgDeepSleepTimeMin = avgDeepSleepTimeMin;
    }

    public Integer getAvgLightSleepTimeMin() {
        return avgLightSleepTimeMin;
    }

    public void setAvgLightSleepTimeMin(Integer avgLightSleepTimeMin) {
        this.avgLightSleepTimeMin = avgLightSleepTimeMin;
    }

    public Integer getAvgAwakeTimeMin() {
        return avgAwakeTimeMin;
    }

    public void setAvgAwakeTimeMin(Integer avgAwakeTimeMin) {
        this.avgAwakeTimeMin = avgAwakeTimeMin;
    }

    public Integer getAvgStepDay() {
        return avgStepDay;
    }

    public void setAvgStepDay(Integer avgStepDay) {
        this.avgStepDay = avgStepDay;
    }
};
