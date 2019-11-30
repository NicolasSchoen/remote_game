package de.nicolasschoen.gamecontroller;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.net.Socket;

public class MainActivity extends AppCompatActivity {

    Button connectButton;
    EditText ipText;
    EditText portText;
    //Socket gameapp;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        connectButton = (Button) findViewById(R.id.button);
        ipText = (EditText) findViewById(R.id.editText);
        portText = (EditText) findViewById(R.id.editText2);

        connectButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                connect(ipText.getText().toString(), portText.getText().toString());
            }
        });
    }

    public void connect(String ipadr, String port){
        //open Controll-Activity
        Intent intent = new Intent(this, Controll.class);
        intent.putExtra("EXTRA_IPADR", ipadr);
        intent.putExtra("EXTRA_PORT", port);
        startActivity(intent);


    }
}
