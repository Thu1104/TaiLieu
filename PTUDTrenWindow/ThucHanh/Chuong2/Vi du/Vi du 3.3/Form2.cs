using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Vi_du_3._3
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        private void btnDangNhap_Click(object sender, EventArgs e)
        {
            string user, pass;
            user = this.txtUser.Text;
            pass = this.txtPass.Text;
            if (user == "teonv" && pass == "123")
                this.Close();
            else if (user != "teonv")
            {
                MessageBox.Show("Không đúng tên người dùng !!", "Thông báo");
                this.txtUser.Focus();
            }
            else
            {
                MessageBox.Show("Không đúng mật khẩu !!", "Thông báo");
                this.txtPass.Focus();
            }
        }

        private void btnThoat_Click(object sender, EventArgs e)
        {
            DialogResult traloi;
            traloi = MessageBox.Show("Chắc không?", "Trả lời", MessageBoxButtons.OKCancel, MessageBoxIcon.Question);
            if (traloi == DialogResult.OK)
                Application.Exit();
        }
    }
}
