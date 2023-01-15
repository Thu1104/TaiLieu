using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace QuanLyBanHang
{
    public partial class FormKhachHang : Form
    {
        string strConnectionString = @"Data Source=.\SQLEXPRESS;Initial Catalog=QuanLyBanHang;Integrated Security=True";
        SqlConnection conn = null;
        SqlDataAdapter daKhachHang = null;
        SqlDataAdapter daThanhPho = null;

        DataTable dtKhachHang = null;
        DataTable dtThanhPho = null;

        void LoadData()
        {
            try
            {
                // Khởi động connection
                conn = new SqlConnection(strConnectionString);
                // Vận chuyển dữ liệu vào DataTable dtThanhPho
                daThanhPho = new SqlDataAdapter("SELECT * FROM THANHPHO", conn);
                dtThanhPho = new DataTable();
                dtThanhPho.Clear();
                daThanhPho.Fill(dtThanhPho);
                // Đưa dữ liệu lên ComboBox trong DataGridView
                (dgvKHACHHANG.Columns["ThanhPho"] as DataGridViewComboBoxColumn).DataSource = dtThanhPho;
                (dgvKHACHHANG.Columns["ThanhPho"] as DataGridViewComboBoxColumn).DisplayMember = "TenThanhPho";
                (dgvKHACHHANG.Columns["ThanhPho"] as DataGridViewComboBoxColumn).ValueMember = "ThanhPho";
                // Vận chuyển dữ liệu vào DataTable dtKhachHang
                daKhachHang = new SqlDataAdapter("SELECT * FROM KHACHHANG", conn);
                dtKhachHang = new DataTable();
                dtKhachHang.Clear();
                daKhachHang.Fill(dtKhachHang);
                // Đưa dữ liệu lên DataGridView
                dgvKHACHHANG.DataSource = dtKhachHang;
            }
            catch (SqlException)
            {
                MessageBox.Show("Không lấy được nội dung trong table KHACHHANG. Lỗi rồi!!!");
            }
        }
        public FormKhachHang()
        {
            InitializeComponent();
        }

        private void FormKhachHang_Load(object sender, EventArgs e)
        {
            LoadData();
        }

        private void FormKhachHang_FormClosing(object sender, FormClosingEventArgs e)
        {
            dtKhachHang.Dispose();
            dtKhachHang = null;
            conn = null;
        }

        private void btnThoat_Click(object sender, EventArgs e)
        {
            DialogResult traloi;
            traloi = MessageBox.Show("Chắc không?", "Trả lời", MessageBoxButtons.OKCancel, MessageBoxIcon.Question);
            if (traloi == DialogResult.OK)
                Application.Exit();
        }

        private void btnReLoad_Click(object sender, EventArgs e)
        {
            LoadData();
        }
    }
}
