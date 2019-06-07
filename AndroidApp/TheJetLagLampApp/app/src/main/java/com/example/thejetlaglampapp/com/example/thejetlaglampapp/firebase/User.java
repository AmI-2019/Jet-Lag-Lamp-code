package com.example.thejetlaglampapp.com.example.thejetlaglampapp.firebase;

public class User {

    String name;
    String surname;
    Integer age;
    String email;
    String home_address;
    String hotel_address;
    Integer white_noise_preference;
    String typicalBedTime;
    String typicalWakeUpTime;
    Integer avgStepDay;
    String tomorrowWakeUpSchedule;
    String todaySleepSchedule;



    public User() {

    }

    public String getTomorrowWakeUpSchedule() {
        return tomorrowWakeUpSchedule;
    }

    public void setTomorrowWakeUpSchedule(String tomorrowWakeUpSchedule) {
        this.tomorrowWakeUpSchedule = tomorrowWakeUpSchedule;
    }

    public String getTodaySleepSchedule() {
        return todaySleepSchedule;
    }

    public void setTodaySleepSchedule(String todaySleepSchedule) {
        this.todaySleepSchedule = todaySleepSchedule;
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

    public String getTypicalBedTime() {
        return typicalBedTime;
    }

    public void setTypicalBedTime(String typicalBedTime) {
        this.typicalBedTime = typicalBedTime;
    }

    public String getTypicalWakeUpTime() {
        return typicalWakeUpTime;
    }

    public void setTypicalWakeUpTime(String typicalWakeUpTime) {
        this.typicalWakeUpTime = typicalWakeUpTime;
    }

    public Integer getAvgStepDay() {
        return avgStepDay;
    }

    public void setAvgStepDay(Integer avgStepDay) {
        this.avgStepDay = avgStepDay;
    }
}
