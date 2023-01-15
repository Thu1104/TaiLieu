//TCP phuc vu song song
import java.io.*;
import java.net.*;
import java.util.Scanner;

public class ClientListThuMuc {
    public static void main(String[] args) {
        try {
            //Ket noi den server
            Scanner kb = new Scanner(System.in);
            System.out.print("Nhap dia chi IP cua server: ");
            String IP = kb.nextLine();
            Socket s = new Socket(IP, 10000);
            System.out.println("Da noi ket den Server co IP " + IP + " bang cong " + s.getPort());
            //Lay ra 2 Stream in - out
            InputStream is = s.getInputStream();
            OutputStream os = s.getOutputStream();
            Scanner sc = new Scanner(is);
            PrintWriter pw = new PrintWriter(os);
            //Nhap tu ban phim ten thu muc can list
            System.out.print("Nhap ten thu muc tren Server can list: ");
            String thumuc = kb.nextLine();
            //Gui yeu cau cho server
            String caulenh = "LIST" + thumuc;
            pw.println(caulenh);
            pw.flush();
            //Nhan n la so luong thanh phan co trong thu muc
            String str = sc.nextLine();
            int n = Integer.parseInt(str);
            if (n == -1) {
                System.out.println("Thu muc khong ton tai");
            }
            else {
                if (n == 0)
                    System.out.println("Thu muc rong");
                else {
                    //Nhan va hien thi tiep n dong (ten thu muc con hoac tap tin)
                    System.out.println("Noi dung thu muc yeu cau gom: ");
                    for (int i = 0; i < n; i++) {
                        String kq = sc.nextLine();
                        System.out.println(kq);
                    }
                }
            }
            s.close();
        } catch (IOException e) {
            System.out.println(e);
        }
    }
}
