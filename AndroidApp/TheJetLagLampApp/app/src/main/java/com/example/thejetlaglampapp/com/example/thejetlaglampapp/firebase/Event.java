package com.example.thejetlaglampapp.com.example.thejetlaglampapp.firebase;

public class Event {
    String title;
    String start_time;
    String end_time;

    public Event(){

    }

    public Event(String title, String start_time, String end_time) {
        this.title = title;
        this.start_time = start_time;
        this.end_time = end_time;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getStart_time() {
        return start_time;
    }

    public void setStart_time(String start_time) {
        this.start_time = start_time;
    }

    public String getEnd_time() {
        return end_time;
    }

    public void setEnd_time(String end_time) {
        this.end_time = end_time;
    }

    @Override
    public String toString() {
        String toReturn=this.title+"\n"+this.start_time +"\n"+this.end_time;
        return toReturn;
    }
}

