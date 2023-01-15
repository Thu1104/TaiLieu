//Socket TCP phuc vu song song
import java.io.*;
import java.net.*;
import java.util.Scanner;
public class ServerListThuMuc {
    public static void main(String[] args) {
        try {
            //Khoi tao server cong 10000
            ServerSocket ss = new ServerSocket(10000);
            System.out.println("Khoi tao thanh cong Server cong 10000");
            while (true) {
                //chap nhan ket noi voi client
                Socket s = ss.accept();
                //lay ra 2 stream in out
                InputStream is = s.getInputStream();
                OutputStream os = s.getOutputStream();
                Scanner sc = new Scanner(is);
                PrintWriter pw = new PrintWriter(os);
                //Nhan cau lenh LIST tu client gui qua
                String caulenh = sc.nextLine();
                //lay ten thu muc theo yeu cau
                String thumuc = caulenh.substring(5);
                //xu ly yeu cau
                File f = new File(thumuc);
                if (f.exists() && f.isDirectory()) {
                    String kq[] = f.list();
                    //Gui ket qua cho client
                    int n = kq.length;
                    pw.println(n);
                    pw.flush();
                    for (int i = 0; i < n; i++) {
                        File f1 = new File(thumuc + "/" + kq[i]);
                        if (f1.isFile()) {
                            pw.println(kq[i]);
                        }
                        else {
                            pw.println("[" + kq[i] + "]");
                        }
                    }
                }
            }

        } catch (IOException e) {
            System.out.println("Loi nhap xuat");
        }
    }
}
