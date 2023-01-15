using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Bai_tap_1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnDung_Click(object sender, EventArgs e)
        {
            DialogResult traloi;
            traloi = MessageBox.Show("Chắc không?", "Trả lời",
            MessageBoxButtons.OKCancel, MessageBoxIcon.Question);
            if (traloi == DialogResult.OK)
                Application.Exit();
        }

        private void btnCong_Click(object sender, EventArgs e)
        {
            float so1 = Convert.ToSingle(this.txtSo1.Text);
            float so2 = Convert.ToSingle(this.txtSo2.Text);
            float kq = so1 + so2;
            txtKQ.Text = kq.ToString();
        }

        private void btnTru_Click(object sender, EventArgs e)
        {
            float so1 = Convert.ToSingle(this.txtSo1.Text);
            float so2 = Convert.ToSingle(this.txtSo2.Text);
            float kq = so1 - so2;
            txtKQ.Text = kq.ToString();
        }

        private void btnNhan_Click(object sender, EventArgs e)
        {
            float so1 = Convert.ToSingle(this.txtSo1.Text);
            float so2 = Convert.ToSingle(this.txtSo2.Text);
            float kq = so1 * so2;
            txtKQ.Text = kq.ToString();
        }

        private void btnChia_Click(object sender, EventArgs e)
        {
            float so1 = Convert.ToSingle(this.txtSo1.Text);
            float so2 = Convert.ToSingle(this.txtSo2.Text);
            float kq = so1 / so2;
            if (so2 == 0)
            {
                MessageBox.Show("Số thứ 2 phải khác 0!", "Thông báo");
                this.txtSo2.Text = "";
                this.txtSo2.Focus();
            }
            else txtKQ.Text = kq.ToString();
        }

        private void btnXoa_Click(object sender, EventArgs e)
        {
            this.txtSo1.Text = "";
            this.txtSo2.Text = "";
            this.txtKQ.Text = "";
        }
    }
}
