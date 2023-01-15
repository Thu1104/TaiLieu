import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.util.Scanner;

class CopyFileNhiPhan {
    public static void main(String[] args) {
        try {
            //Nhap ten
            Scanner kb = new Scanner(System.in);
            System.out.print("Nhap ten file can doc: ");
            String filedoc = kb.nextLine();
            System.out.print("Nhap ten file can ghi: ");
            String fileghi = kb.nextLine();
            //Doc file
            File ff = new File(filedoc);
            int len = (int) ff.length();
            System.out.println("Kich thuoc file: " + len);
            FileInputStream f1 = new FileInputStream(filedoc);
            DataInputStream f2 = new DataInputStream(f1);
            byte b[] = new byte[len];
            f2.readFully(b);
            System.out.println("Da doc xong noi dung file");
            //Ghi file
            FileOutputStream f3 = new FileOutputStream(fileghi);
            DataOutputStream f4 = new DataOutputStream(f3);
            f4.write(b);
            f1.close();
            f2.close();
            System.out.println("Da ghi file thanh cong");
        }
        catch (Exception e) {
            System.out.println("Khong tim thay file");
        }
    }
}