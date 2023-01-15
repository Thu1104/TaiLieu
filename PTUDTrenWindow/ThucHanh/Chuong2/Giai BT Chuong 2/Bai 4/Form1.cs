using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Bai_4
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

        private void btnXoa_Click(object sender, EventArgs e)
        {
            this.txtHoTen.Clear();
            this.chkNu.Checked = false;
            this.txtVan.Clear();
            this.txtToan.Clear();
            this.txtNN.Clear();
            this.txtDTN.Clear();
            this.txtDThem.Text = "0";
            this.txtKQ.Clear();
            this.txtXL.Clear();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            this.chkNu.Checked = false;
            this.txtDThem.Text = "0";
        }
        private void chkNu_CheckedChanged(object sender, EventArgs e)
        {
            if (chkNu.Checked == true)
                this.txtDThem.Text = "0.5";
            else
                this.txtDThem.Text = "0";
        }
        private void txtDThem_TextChanged(object sender, EventArgs e)
        {
       
        }

        private void btnTinh_Click(object sender, EventArgs e)
        {
            float diemVan = Convert.ToSingle(this.txtVan.Text);
            float diemToan = Convert.ToSingle(this.txtToan.Text);
            float diemNN = Convert.ToSingle(this.txtNN.Text);

            float min = diemVan;
            if (diemToan < min) min = diemToan;
            if (diemNN < min) min = diemNN;
            txtDTN.Text = min.ToString();

            float diemThem = Convert.ToSingle(this.txtDThem.Text);
            float kq = diemVan * 2 + diemToan * 2 + diemNN + diemThem;
            txtKQ.Text = kq.ToString();

            string loai = "";
            if (kq >= 40 && min >= 7)
                loai = "Giỏi";
            else if (kq >= 35 && min >= 6)
                loai = "Khá";
            else if (kq >= 25 && min >= 5)
                loai = "Trung bình";
            else loai = "Yếu";
            txtXL.Text = loai.ToString();
        }

        private void btnTroVe_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
