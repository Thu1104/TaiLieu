import java.io.*;
import java.net.*;
import java.util.Scanner;
public class UDPFileClient {
    public static void main(String[] args) {
        try{
            //Tao UDP Socket
            DatagramSocket ds = new DatagramSocket();
            //Nhap dia chi server va ten file can lay
            Scanner kb = new Scanner(System.in);
            System.out.print("Nhap dia chi server: ");
            String dcServer = kb.nextLine();
            System.out.println("Nhap duong dan va file can lay: ");
            String tenfile = kb.nextLine();
            //Dong goi yeu cau
            String yeucau = "READUDP " + tenfile;
            byte b[] = yeucau.getBytes();
            int len = b.length;
            InetAddress ad = InetAddress.getByName(dcServer);
            int p = 9999;
            DatagramPacket goigui = new DatagramPacket(b, len, ad, p);
            //gui goi
            ds.send(goigui);
            //Nhan goi ket qua
            byte b1[] = new byte[64000];
            DatagramPacket goinhan = new DatagramPacket(b1, 64000);
            ds.receive(goinhan);
            //Luu ket qua
            byte b2[] = goinhan.getData();
            int len2 = goinhan.getLength();
            if (len2 == 0) {
                System.out.println("File khong ton tai hoac file rong");
            }
            else {
                System.out.print("Nhap ten file can luu");
                String tenfileluu = kb.nextLine();
                FileOutputStream f = new FileOutputStream(tenfileluu);
                f.write(b2, 0, len2);
                f.close();
                System.out.println("Da ghi file thanh cong");
            }
            ds.close();
        } catch (IOException e) {
            System.out.println(e);
        }
    }
}
