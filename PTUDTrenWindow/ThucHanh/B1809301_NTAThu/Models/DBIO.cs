using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace B1809301_NTAThu.Models
{
    public class DBIO
    {
        B1809301_NTAThuEntities mydb = new B1809301_NTAThuEntities();
        public List<SANPHAM> getList_SANPHAM()
        {
            //access to the SANPHAM table to read all rows
            return mydb.SANPHAMs.ToList();
        }
 
        //hàm getObject_SANPHAM(string id) trả về một quyển sách theo id 
        public SANPHAM getObject_SANPHAM(string id)
         {
            //biểu thức so sánh có cú pháp như C#
            //chứ không phải của SQL
            return mydb.SANPHAMs.Where(c => c.MASP == id).FirstOrDefault();
         }
        //hàm addObject_SANPHAM(SANPHAM s) thêm vào một quyển sách
         public void addObject_SANPHAM(SANPHAM s)
         {
             mydb.SANPHAMs.Add(s);
             mydb.SaveChanges();
         }
          //hàm editObject_SANPHAM(SANPHAM s) sửa một quyển sách
         public void editObject_SANPHAM(SANPHAM s)
         {
             SANPHAM x = getObject_SANPHAM(s.MASP);
             x.TENSP = s.TENSP;
             x.NGAYCAPNHAT = s.NGAYCAPNHAT;
             x.TINHTRANG = s.TINHTRANG;
             x.MOTA = s.MOTA;
             x.DONVITINH = s.DONVITINH;
             x.DONGIA = s.DONGIA;
             mydb.SaveChanges();
         }
        //hàm deleteObject_SANPHAM(SANPHAM s) xóa một quyển sách s
         public void deleteObject_SANPHAM(SANPHAM s)
         {
             SANPHAM x = getObject_SANPHAM(s.MASP);
             mydb.SANPHAMs.Remove(x);
             mydb.SaveChanges();
         }
    }
}