using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class PlayerController : MonoBehaviour
{
    public Rigidbody rb;
    public float speed = 2;
    public float jump = 200;
    public static int Points;
    public Text PointsText;
    public bool isGrounded;

    public void AddPoints(int points)
    {
        PointsText.text += $"Points:{points}";
    }
    // Start is called before the first frame update
    void Start()
    {
        PointsText.text = $"Points:{Points}";
    }
    private void OnCollisionStay(Collision collision)
    {
        if(collision.gameObject.tag == "Ground")
        {
            isGrounded = true;
        }
    }

    private void OnCollisionExit(Collision collision)
    {
        if(collision.gameObject.tag == "Ground")
        {
            isGrounded = false;
        }
    }
     
    // Update is called once per frame
    void Update()
    {
        float vertical = Input.GetAxis("Vertical");
        float horizontal = Input.GetAxis("Horizontal");
        Vector3 force = new Vector3(horizontal, 0, vertical);
        rb.AddForce(force * speed);
        if (Input.GetKeyDown(KeyCode.Space) && isGrounded)
        {
            rb.AddForce(Vector3.up * jump);
        }
    }
}
