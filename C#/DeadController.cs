using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
// Тригер смерти
public class DeadController : MonoBehaviour
{
    public int DeathPenalty = 5;
    public int CurrentSceneIndex = 0;
    void OnTriggerEnter(Collider collider)
    {
        if (collider.tag == "Player")
        {
            PlayerController.Points -= DeathPenalty;
            SceneManager.LoadScene(CurrentSceneIndex);
        }
    }



}
