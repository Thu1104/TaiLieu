import java.io.*;
import java.net.*;
import java.util.Scanner;
public class TCPClient {
    public static void main(String[] args) {
        try{
            Scanner kb = new Scanner(System.in);
            System.out.print("Nhap dia chi IP server: ");
            String IP = kb.nextLine();
            Socket s = new Socket(IP, 3000);
            InputStream is = s.getInputStream();
            OutputStream os = s.getOutputStream();
            Scanner sc = new Scanner(is);
            PrintWriter pw = new PrintWriter(os);
            //lay file
            System.out.println("Nhap ten thu muc can list");
            String thumuc = kb.nextLine();
            //gui cho server
            String caulenh = "LIST" + thumuc;
            pw.println(caulenh);
            pw.flush();
            //nhan n al so thanh phan co trong thu muc
            String str = kb.nextLine();
            int n = Integer.parseInt(str);
            if(n==-1){
                System.out.println("Thu muc khong ton tai");
            }
            else {
                if(n==0){
                    System.out.println("Thu muc rong");
                }
                else {
                    System.out.println("Noi dung thu muc yeu cau: ");
                    for(int i=0; i<n; i++){
                        String ketqua = kb.nextLine();
                        System.out.print(ketqua);
                    }
                }
            }
            s.close();
        }
    }
}
