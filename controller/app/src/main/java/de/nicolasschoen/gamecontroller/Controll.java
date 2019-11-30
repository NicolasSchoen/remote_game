package de.nicolasschoen.gamecontroller;

import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintStream;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;

public class Controll extends AppCompatActivity {

    Button upButton;
    Button downButton;
    Button rightButton;
    Button leftButton;
    String ipadr;
    String port;
    Socket appsocket;
    PrintWriter out;
    BufferedReader in;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_controll);

        upButton = (Button) findViewById(R.id.button2);
        downButton = (Button) findViewById(R.id.button3);
        rightButton = (Button) findViewById(R.id.button4);
        leftButton = (Button) findViewById(R.id.button5);
        ipadr = getIntent().getStringExtra("EXTRA_IPADR");
        port = getIntent().getStringExtra("EXTRA_PORT");

        try {
            //appsocket = new Socket(ipadr, Integer.parseInt(port));
            //out = new PrintWriter(appsocket.getOutputStream());
            //in = new BufferedReader(new InputStreamReader(appsocket.getInputStream()));
            //out.println("start");
            //out.flush();
            //out.writeUTF("start");
            //in.readLine();
        }
        catch (Exception e){
            String text = "Error: " + ipadr + " : " + port + e.toString();
            Toast.makeText(getApplicationContext(), text, Toast.LENGTH_SHORT ).show();
            finish();
        }

        upButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                up();
            }
        });
        downButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                down();
            }
        });
        rightButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                right();
            }
        });
        leftButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                left();
            }
        });
    }

    public void up(){
        try {
            //out.println("up");
            //out.flush();
            //in.readLine();

            MyClientTask myClientTask = new MyClientTask(
                    ipadr,
                    Integer.parseInt(port));
            myClientTask.execute("up");

        }
        catch (Exception e){

        }

    }

    public void down(){
        try {
            //out.println("down");
            //out.flush();
            //in.readLine();
            MyClientTask myClientTask = new MyClientTask(
                    ipadr,
                    Integer.parseInt(port));
            myClientTask.execute("down");
        }
        catch (Exception e){

        }
    }

    public void right(){
        try {
            //out.println("right");
            //out.flush();
            //in.readLine();
            MyClientTask myClientTask = new MyClientTask(
                    ipadr,
                    Integer.parseInt(port));
            myClientTask.execute("right");
        }
        catch (Exception e){

        }
    }

    public void left(){
        try {
            //out.println("left");
            //out.flush();
            //in.readLine();
            MyClientTask myClientTask = new MyClientTask(
                    ipadr,
                    Integer.parseInt(port));
            myClientTask.execute("left");
        }
        catch (Exception e){

        }
    }







    public class MyClientTask extends AsyncTask<String, Void, Void> {

        String dstAddress;
        int dstPort;
        String response;

        MyClientTask(String addr, int port) {
            dstAddress = addr;
            dstPort = port;
        }

        @Override
        protected Void doInBackground(String... params) {
            try {
                Socket socket = new Socket(dstAddress, dstPort);

                OutputStream outputStream = socket.getOutputStream();
                PrintStream printStream = new PrintStream(outputStream);
                printStream.print(params[0]);

                socket.close();

            } catch (UnknownHostException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            } catch (IOException e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }
            return null;
        }

    }
}
