using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
// Скрипт на финиш(Можно переработать в спавн) 
public class FinishController: MonoBehaviour
{
    public int NextSceneIndex = 1;
    void Start()
    {

    }


    void Update()
    {

    }
    private void OnTriggerEnter(Collider other)
    {
        if (other.gameObject.tag == "Player")
        {
            var pc = other.gameObject.GetComponent<PlayerController>();
            pc.AddPoints(10);
            ButtonController.Instance.ShowFinish();
        }
    }
}
