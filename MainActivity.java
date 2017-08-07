package googlemaps.flatfisher.com.mytestapp;

import android.content.Context;
import android.net.wifi.WifiConfiguration;
import android.net.wifi.WifiManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;

import java.util.List;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        WifiManager manager = (WifiManager)getSystemService(WIFI_SERVICE);
        int wifiState = manager.getWifiState();
        if(wifiState == WifiManager.WIFI_STATE_DISABLED){
            manager.setWifiEnabled(true); //true or false
        }
        List<WifiConfiguration> cfgList = manager.getConfiguredNetworks();
        if(cfgList != null) {
            String[] nets = new String[cfgList.size()];
            for (int i = 0; i < cfgList.size(); i++) {
                nets[i] = String.format("Network ID:%4d\nSSID:%s", cfgList.get(i).networkId, cfgList.get(i).SSID);
            }
            for(String str : nets){
                Log.v("abe", str);
            }
        }
        if(wifiState == WifiManager.WIFI_STATE_DISABLED){
            manager.setWifiEnabled(false); //true or false
        }

    }
}
