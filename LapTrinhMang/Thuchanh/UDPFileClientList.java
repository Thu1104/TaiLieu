import java.io.*;
import java.net.*;
import java.util.Scanner;
public class UDPFileClientList {
    public static void main(String[] args) {
        try{
            DatagramSocket ds = new DatagramSocket();
            Scanner kb = new Scanner(System.in);
            System.out.println("Nhap dia chi IP: ");
            String IP = kb.nextLine();
            System.out.println("Nhap ten file can lay: ");
            String tenfile = kb.nextLine();
            //gui
            String yeucau = "READUDP" + tenfile;
            byte b[] = yeucau.getBytes();
            int n = b.length;
            InetAddress ad = InetAddress.getByName(IP);
            int p =9999;
            DatagramPacket goigui = new DatagramPacket(b, n, ad, p);
            ds.send(goigui);
            byte b1[] = new byte[64000];
            DatagramPacket goinhan = new DatagramPacket(b1, 64000);
            ds.receive(goinhan);
            byte b2[] = goinhan.getData();
            int len2 = goinhan.getLength();
            if(len2==0){
                System.out.println("file khong ton tai hoac file rong");
            }
            else{
                System.out.println("nhap ten file can luu");
                String tenfileluu = kb.nextLine();
                FileOutputStream f = new FileOutputStream(tenfileluu);
                f.write(b2, 0, len2);
                f.close();
                System.out.println("da ghi file thanh cong");
            }
            ds.close();
        }
    }
}
