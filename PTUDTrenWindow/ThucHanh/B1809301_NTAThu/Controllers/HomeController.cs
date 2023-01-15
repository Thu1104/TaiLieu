using B1809301_NTAThu.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace B1809301_NTAThu.Controllers
{
    public class HomeController : Controller
    {
        DBIO db = new DBIO();
        // GET: Home
        public ActionResult Index()
        {
            List<SANPHAM> list = db.getList_SANPHAM();
            return View(list);
        }
        public ActionResult Create()
        {
            return View();
        }
        //Khi gọi đến phương thức addObject_SANPHAM(SANPHAM s) in DBIO.cs
        //thì đồng thời ta cần một thông điệp nào đó để nó load dữ liệu lên
        //=> dùng [HttpPost]
        [HttpPost]
        public ActionResult Create(SANPHAM s)
        {
            db.addObject_SANPHAM(s);
            //sau khi thêm rồi, ta điều hướng người dùng đến trang Index
            return RedirectToAction("Index");
        }
        //Sửa sách phức tạp hơn thêm (create) vì ta cần biết sửa sách nào? 
        //Ta cần biết id của quyển sách bạn đang định sửa
        public ActionResult Edit(string id)
        {
            SANPHAM s = db.getObject_SANPHAM(id);
            return View(s); //lấy ra quyển sách thì sau đó mới sửa được
        }
        [HttpPost] //Ý nghĩa là khi bạn gọi Edit nó cần gửi lên thông điệp để sửa thông tin này 
        public ActionResult Edit(SANPHAM s) //phải đặt tên là Edit như hàm bên trên, không dùng tên khác
        {
            db.editObject_SANPHAM(s);
            return RedirectToAction("Index"); //Khi sửa rồi thì hệ thống sẽ điều hướng quay về trang chủ
        }
        //Xóa một quyển sách
        //Ta cần biết id của quyển sách bạn đang định xóa
        public ActionResult Delete(string id)
        {
            SANPHAM s = db.getObject_SANPHAM(id);
            return View(s); //lấy ra quyển sách thì sau đó mới xóa được
        }
        [HttpPost] //Ý nghĩa là khi bạn gọi Delete nó cần gửi lên thông điệp để xóa thông tin này 
        public ActionResult Delete(SANPHAM s)
        {
            db.deleteObject_SANPHAM(s);
            return RedirectToAction("Index"); //Khi xóa rồi thì hệ thống sẽ điều hướng quay về trang chủ
        }
        //Xem một quyển sách
        //Ta cần biết id của quyển sách bạn đang định xem chi tiết
        public ActionResult Details(string id)
        {
            SANPHAM s = db.getObject_SANPHAM(id);
            return View(s); //lấy ra quyển sách cần xem
        }
    }
}